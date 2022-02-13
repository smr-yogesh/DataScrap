import pandas as pd
import os

outpath='data.json'

if (os.path.exists('data.json')):
    os.remove('data.json')
dfs = pd.read_html('https://www.nepalipaisa.com/StockLive.aspx')
len(dfs)
df = dfs[0]
df.head
df
df.drop(['LTV','Quantity','Difference Rs.','No of Transaction'], axis=1, inplace=True)
df.rename(columns={'Closing Price' : 'Closing', 'Max Price' : 'High', 'Min Price' : 'Low', 'Opening Price' : 'Open', '%Change':'Change'}, inplace=True)
#print(df)
#df.to_excel('data.xlsx')
print('Data acquired')
Symbols = df.Symbols
Closing = df.Closing
Change = df.Change
High = df.High
Low = df.Low
Open = df.Open

container = { }

i = 0
while i< len(Symbols):
    container[Symbols[i]] = [
        {"Open:": Closing[i]},
        {"High:": High[i]},
        {"Low:": Low[i]},
        {"Closing Price:": Closing[i]},
        {"Change:": Change[i]}
    ]
    i = i +1
df = pd.DataFrame(container)
df.to_json(outpath, indent=4)
print('Data converted')