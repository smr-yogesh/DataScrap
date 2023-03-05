from datetime import datetime, timedelta

from flask import Blueprint, jsonify, render_template, request

from auth import token_required
from routes import app
from scrape import read_nepse_data

B_gui = Blueprint('B_gui', __name__)

@B_gui.route('/')
def home_page():
    nepse = read_nepse_data()
    return render_template('index.html', nepse = nepse, date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))