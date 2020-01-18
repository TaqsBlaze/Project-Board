from flask import Flask
from flask_sqlalchemy import SQLAlchemy



App = Flask(__name__)
App.config['SECRET_KEY'] = '2582ec1d875514668349f162e3b4e71c65c1'
App.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db = SQLAlchemy(App)
from LeNode.Routes import routes