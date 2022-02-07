import pandas as pd


dfs = pd.read_html('https://www.nepalipaisa.com/StockLive.aspx')
len(dfs)
df = dfs[0]
df.head
df
df.drop(['LTV','Quantity','Difference Rs.','No of Transaction'], axis=1, inplace=True)
df.rename(columns={'Closing Price' : 'Closing', 'Max Price' : 'High', 'Min Price' : 'Low', 'Opening Price' : 'Open', '%Change':'Change'}, inplace=True)
df.to_excel('output.xlsx')