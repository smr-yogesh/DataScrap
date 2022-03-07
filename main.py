from flask import *
import json, time
import os
from jinja2 import environment, FileSystemLoader
app = Flask(__name__)

with open("data/data.json","r") as d:
    nepse = json.load(d)

@app.route('/')
def home_page():
    return render_template('index.html',nepse = nepse)

@app.route('/api')
def api():
    return jsonify(nepse)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')