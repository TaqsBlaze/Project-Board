from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


App = Flask(__name__)
App.config['SECRET_KEY'] = '2582ec1d875514668349f162e3b4e71c65c1'
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/info.db'
db = SQLAlchemy(App)
bcrypt = Bcrypt(App)
from LeNode.Routes import routes