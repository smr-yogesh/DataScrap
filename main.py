
from flask import *
import json, time


app = Flask(__name__)
f = open('data.json')
data = json.load(f)
@app.route('/', methods=['GET'])
def home_page():
    return (data)

if __name__ == '__main__':
    app.run(port=5000)