from flask import render_template,url_for,redirect,flash
from LeNode.Models.models import User, Post
from LeNode.forms.Forms import LoginForm,RegistrationForm,PostForm,UpdateProfile
from LeNode import app
from LeNode import db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required
projects = [
    {'title':'Softaz',
     'about':'A software research program working on making peoples lives through technology',
     'Author':'Softaz'
     },
    {'title':'Softaz',
     'about':'A software research program',
     'Author':'Softaz'
     },
    {'title':'Softaz',
     'about':'A software research program',
     'Author':'Softaz'
     }
]
@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def index():
    form = LoginForm()
    
    if(form.validate_on_submit()):
        user = User.query.filter_by(username=form.user.data).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
    return render_template("index.html",title = 'Index',form=form)


@app.route("/home",methods=['GET','POST'])
@login_required
def home():
    return render_template("home.html",title='Home',projects=projects)


@app.route("/profile",methods=['GET','POST'])
@login_required
def profile():
    post_form = UpdateProfile()
    return render_template("profile.html",form=post_form,projects=projects)

@app.route("/register",methods=['GET','POST'])
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

@app.route("/newpost",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if(form.validate_on_submit()):
        pass
    return render_template("createpost.html",title="New Post",form=form)