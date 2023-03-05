from flask import Flask
import os

app = Flask(__name__)
template_dir = os.path.abspath('D:\LAB\Development\Data_Scrap\\templates')
app.template_folder = template_dir
app.config["SECRET_KEY"] = 'thisisthekey'