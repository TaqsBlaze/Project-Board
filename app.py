from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import Forms
from datetime import datetime

App = Flask(__name__)
App.config['SECRET_KEY'] = '360b8407aa09acb8'
App.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db = SQLAlchemy(App)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    profile_pic = db.Column(db.String(20),unique=False,default='default.png')
    password = db.Column(db.String(60),nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_pic}')"
    
class Post(db.Model):
     id = db.Column(db.Integer,primary_key = True)
     title = db.Column(db.String(100),nullable=False)
     date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
     post = db.Column(db.Text,nullable=False)
     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
     
     def __repr__(self):
         return f"Post('{self.title}','{self.post}')"
@App.route("/")
@App.route("/index")
def index():
    form = Forms.LoginForm()
    if(form.validate_on_submit()):
        return redirect(url_for('home'))
    return render_template("index.html",title = 'Index',form=form)
@App.route("/home")
def home():
	form = Forms.Post()
	return render_template("home.html",title='Home',form=form)


@App.route("/profile")
def profile():
	return render_template("profile.html")

@App.route("/register")
def register():
    form = Forms.RegistrationForm()
    return render_template("register.html",title="register",form=form)
if(__name__ == "__main__"):
	App.run(debug = True)
