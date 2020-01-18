from flask import render_template,url_for,redirect,flash
from LeNode.Models.models import User, Post
from LeNode.forms.Forms import LoginForm,RegistrationForm,PostForm
from LeNode import App
from LeNode import db,bcrypt

@App.route("/",methods=['GET','POST'])
@App.route("/index",methods=['GET','POST'])
def index():
    form = LoginForm()
    user = User.query.filter_by(username=form.user.data).first()
    if(form.validate_on_submit()):
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            return redirect(url_for('home'))
    return render_template("index.html",title = 'Index',form=form)


@App.route("/home",methods=['GET','POST'])
def home():
    form = Post()
    return render_template("home.html",title='Home',form=form)


@App.route("/profile",methods=['GET','POST'])
def profile():
    return render_template("profile.html")

@App.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,email=form.email.data,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!','success')
            return redirect('index')
        except Exception as e:
            return f"Could not create User<br> {e}"
    return render_template("register.html",title="register",form=form)
