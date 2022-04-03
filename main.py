from distutils.log import error
from flask import *
import json, time
import os, sys
from jinja2 import environment, FileSystemLoader
app = Flask(__name__)

def read_nepse_data():
    os.system("scrape.py")
    with open("data/data.json","r") as d:
        nepse = json.load(d)
        return nepse 

@app.route('/')
def home_page():
    nepse = read_nepse_data()
    return render_template('index.html',nepse = nepse)

@app.route('/api')
def api():
    nepse = read_nepse_data()
    return jsonify(nepse)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

