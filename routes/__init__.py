from flask import Flask
import os

app = Flask(__name__)
app.template_folder = app.template_folder = '../templates'
app.config["SECRET_KEY"] = 'thisisthekey'