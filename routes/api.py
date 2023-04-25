from flask import request, jsonify, Blueprint, render_template
from datetime import datetime, timedelta
from auth import token_required
from routes import app
from engine import read_nepse_data
import jwt

B_api = Blueprint('B_api', __name__)

@B_api.route('/get_token', methods=['POST','GET'])
def get_token():
    return render_template('token.html')

@B_api.route('/api_pass', methods=['POST','GET'])
def api_pass():
    time = int(request.form['time'])
    code = request.form['passcode']
    if code == 'edithere':
        token = jwt.encode({'exp' : datetime.utcnow() + timedelta(minutes= time)}, app.config["SECRET_KEY"], algorithm='HS256')
        return render_template ('token.html', token=token.encode().decode('utf-8'))
    
    return render_template ('token.html', token="invalid passcode")

@B_api.route('/api')
@token_required
def api():
    nepse = read_nepse_data()
    return jsonify(nepse)