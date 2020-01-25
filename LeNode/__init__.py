from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2582ec1d875514668349f162e3b4e71c65c1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/info.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from LeNode.Routes import routes