import pandas as pd
import os
import json

from sqlalchemy import true

outpath='data/data.json'

if (os.path.exists(outpath)):
    os.remove('data/data.json')

dfs = pd.read_html('https://www.nepalipaisa.com/StockLive.aspx')
len(dfs)
df = dfs[0]
df.head
df
df.drop(['LTV','Quantity','Difference Rs.','No of Transaction'], axis=1, inplace=True)
df.rename(columns={'Closing Price' : 'Closing', 'Max Price' : 'High', 'Min Price' : 'Low', 'Opening Price' : 'Open', '%Change':'Change'}, inplace=True)
#print(df)
df.to_json(outpath, indent=4,orient='records') #orient='records'

