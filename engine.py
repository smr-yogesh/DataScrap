import pandas as pd
import os, json, sqlite3, datetime, time
from sqlalchemy import true


outpath='data\data.json'
def scrape():
    if (os.path.exists(outpath)):
        os.remove(outpath)

    dfs = pd.read_html('https://www.nepalipaisa.com/StockLive.aspx')
    len(dfs)
    df = dfs[0]
    df.head
    df
    df.drop(['LTV','Quantity','Difference Rs.','No of Transaction'], axis=1, inplace=True)
    df.rename(columns={'Closing Price' : 'Closing', 'Max Price' : 'High', 'Min Price' : 'Low', 'Opening Price' : 'Open', '%Change':'Change'}, inplace=True)
    #print(df)
    df.to_json(outpath, indent=4,orient='records')
    return df

def read_nepse_data():
    scrape()
    with open("data\data.json","r") as d:
        nepse = json.load(d)
        return nepse 

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
