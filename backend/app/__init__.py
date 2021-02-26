from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL


app = Flask(__name__)
CORS(app, resources={r"/queryMarketplace": {"origins": "*"}})
app.config.from_object('config')

mysql = MySQL(app)


from app.controllers import search


