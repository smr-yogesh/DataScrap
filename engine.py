import os, json, sqlite3, datetime, time
from sqlalchemy import true
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

outpath='data\data.json'
async def scrape():
    if (os.path.exists(outpath)):
        os.remove(outpath)
    
    # Launch a headless instance of Pyppeteer
    browser = await launch(headless=True)

    # Create a new page
    page = await browser.newPage()

    # Navigate to the webpage
    await page.goto("https://www.nepalipaisa.com/live-market")

    # Wait for the table to load
    await page.waitForSelector('.table.table-responsive')

    # Get the page source
    html = await page.content()

    # Close the browser
    await browser.close()

    # Parse the html using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table
    table = soup.find('table', {'class': 'table table-responsive'})

    # Extract data from the table
    headers = ["Symbols","Closing","Chg","Change","High","Low","Open","Qty","Txn *"]
    rows = []
    for row in table.find_all('tr'):
        rows.append([cell.text.strip() for cell in row.find_all('td')])

    # Combine headers and data into a list of dictionaries
    data = []
    for row in rows[1:]:
        data.append(dict(zip(headers, row)))

    # Convert string numbers in float values
    for row in data:
        row['Closing'] = float(row['Closing'].replace(',', ''))
        row['Chg'] = float(row['Chg'].replace(',', ''))
        row['Change'] = float(row['Change'].replace(',', ''))
        row['High'] = float(row['High'].replace(',', ''))
        row['Low'] = float(row['Low'].replace(',', ''))
        row['Open'] = float(row['Open'].replace(',', ''))
        row['Qty'] = float(row['Qty'].replace(',', ''))
        row['Txn *'] = float(row['Txn *'].replace(',', ''))

    # Save data to JSON file
    with open(outpath, 'w') as f:
        json.dump(data, f, indent=4)
asyncio.get_event_loop().run_until_complete(scrape())

def read_nepse_data():
    scrape()
    with open("data\data.json","r") as d:
        nepse = json.load(d)
        return nepse 

#below this is experimental and contains heavy bugs and unnecessary code.
conn = sqlite3.connect('data.db')
date = datetime.datetime.now().strftime("%x")
table_name = f"T_{date.replace('/', '_')}"

def set_database():
    c = conn.cursor()
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (symbols text, Closing number, Change number, High number, Low number, Open number)")
    conn.commit()

def data_to_database():
    while true:
        set_database()
        scrape().to_sql(f'{table_name}', conn, if_exists='replace', index = False)
        print("Job done \n\nTime to sleep")
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        noon = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=12, minute=0, second=0)
        if now>=noon:
            noon += datetime.timedelta(days=1)
        time_to_sleep = (noon - now).total_seconds()
        
        # Sleep for the calculated time
        time.sleep(time_to_sleep)
