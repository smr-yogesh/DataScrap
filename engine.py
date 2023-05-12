import os
import json
import sqlite3
import datetime
import time
from sqlalchemy import true
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

counter = 1
outpath = 'data\data.json'
while true:
    print(f"Attempt {counter}")

    async def scrape():
        # Launch a headless instance of Pyppeteer
        browser = await launch(headless=True)
        # browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])

        # Create a new page
        page = await browser.newPage()

        # Navigate to the webpage
        await page.goto("https://www.nepalipaisa.com/live-market")

        # Wait for the table to load
        await page.waitForSelector('.bg-positive-lv-1', {'timeout': 50000})

        # Get the page source
        html = await page.content()

        # Close the browser
        await browser.close()

        # Parse the html using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Find the table
        table = soup.find('table', {'class': 'table table-responsive'})

        # Extract data from the table
        headers = ["Symbol", "Closing", "Chg", "Change",
                   "High", "Low", "Open", "Qty", "Txn *"]
        rows = []
        for row in table.find_all('tr'):
            rows.append([cell.text.strip() for cell in row.find_all('td')])

        # Combine headers and data into a list of dictionaries
        data = []
        for row in rows[1:]:
            data.append(dict(zip(headers, row)))

        try:
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

            if (os.path.exists(outpath)):
                os.remove(outpath)

            # Save data to JSON file
            with open(outpath, 'w') as f:
                json.dump(data, f, indent=4)

        except:
            print("Couldn't extract data")

    counter += 1
    time.sleep(600)
    asyncio.get_event_loop().run_until_complete(scrape())
