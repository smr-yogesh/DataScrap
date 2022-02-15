
from importlib.abc import FileLoader
from msilib.schema import Environment
from unittest import loader
from flask import *
import json, time
from jinja2 import environment, FileSystemLoader
app = Flask(__name__)

with open("data/data.json","r") as d:
    nepse = json.load(d)

@app.route('/')
def home_page():
    return render_template('index.html',nepse = nepse)

if __name__ == '__main__':
    app.run(port=5000)