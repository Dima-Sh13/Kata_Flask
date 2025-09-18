from flask import Flask
app = Flask(__name__)
from app_expenses.routes import *



#set FLASK_APP = main.py
#flask --app main --debug run