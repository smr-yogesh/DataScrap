from flask import request, jsonify, Blueprint
from datetime import datetime, timedelta
from auth import token_required
from routes import app
from scrape import read_nepse_data
import jwt

B_api = Blueprint('B_api', __name__)

@B_api.route('/api_pass')
def api_pass():
    token = jwt.encode({'exp' : datetime.utcnow() + timedelta(minutes= 30)}, app.config["SECRET_KEY"], algorithm='HS256')
    return jsonify({'token':token.encode().decode('utf-8')})

@B_api.route('/api')
@token_required
def api():
    nepse = read_nepse_data()
    return jsonify(nepse)