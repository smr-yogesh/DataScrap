import pandas as pd


dfs = pd.read_html('https://www.nepalipaisa.com/StockLive.aspx')
len(dfs)
df = dfs[0]
df.head
df
df.to_excel('output.xlsx')