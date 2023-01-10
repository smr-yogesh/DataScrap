from datetime import datetime
from distutils.log import error
from flask import *
import json, time
import os, sys, subprocess
from jinja2 import environment, FileSystemLoader
app = Flask(__name__)
from scrape import scrape
def read_nepse_data():
    scrape()
    #os.system("python Data_Scrap/scrape.py")
    with open("data\data.json","r") as d:
        nepse = json.load(d)
        return nepse 

@app.route('/')
def home_page():
    nepse = read_nepse_data()
    return render_template('index.html', nepse = nepse, date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

@app.route('/api')
def api():
    nepse = read_nepse_data()
    return jsonify(nepse)

@app.route('/reqdata')
def reqdata():
    with open('Data_Scrap/data/data.json') as f:
        data = json.load(f)
        value = data[2]
    return jsonify(value)

@app.route('/error')
def error():
    return os._exit(0)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

