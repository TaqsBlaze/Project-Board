from flask import render_template,url_for,redirect
from LeNode.models import User, Post
from LeNode.Forms import LoginForm,RegistrationForm,PostForm
from LeNode import App

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