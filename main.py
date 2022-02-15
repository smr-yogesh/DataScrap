
from turtle import heading
from flask import *
import json, time
from flask import Blueprint, render_template
import pandas as pd

app = Flask(__name__)

heading = ("Symbols", "Closing", "Change", "High", "Low", "Open")
#f = open('data/data.json')
#data = json.loads(f)
with open('data.json','r') as f:
    data = json.load(f) 
symbols = (data['Symbols'])
closing = (data['Closing'])
change = (data['Change'])
high = (data['High'])
low = (data['Low'])
open = (data['Open'])
#data = pd.read_excel('data.xlsx')

@app.route('/')
def table():
    return render_template("index.html", headings = heading, sy = symbols, cl = closing, ch = change, hi = high,lo = low, op = open)

def get_data():
    return data
if __name__ == '__main__':
    app.run(port=5000)