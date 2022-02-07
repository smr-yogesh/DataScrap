from typing import Container
import pandas as pd

datapath= 'output.xlsx'
outpath='data.json'
data = pd.read_excel(datapath)

Symbols = data.Symbols
Closing = data.Closing
Change = data.Change
High = data.High
Low = data.Low
Open = data.Open

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