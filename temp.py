import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize the webdriver
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get("https://www.nepalipaisa.com/live-market")

# Wait for the table to load
driver.implicitly_wait(10)

# Get the page source
html = driver.page_source

# Close the webdriver
driver.quit()

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

# Save data to JSON file
with open('market_data.json', 'w') as f:
    json.dump(data, f, indent=4)
