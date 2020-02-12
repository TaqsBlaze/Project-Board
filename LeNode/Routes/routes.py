from flask import render_template,url_for,redirect,flash,request
from LeNode.Models.models import User, Post
from LeNode import app
import secrets
import os
from LeNode import db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required


@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def index():
    form = LoginForm()

    if(form.validate_on_submit()):
        user = User.query.filter_by(username=form.user.data).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
    return render_template("index.html",form=form)


@app.route("/home",methods=['GET','POST'])
@login_required
def home():
    '''
    Home route
    '''
    search_form = Search()
    if(search_form.validate_on_submit()):
        search = User.query.filter_by(username=search_form.search.data)
        return redirect(url_for("home"))
    else:
        search = None
    return render_template("home.html",title='Home',search_form=search_form,search=search)


def save_image(form_image):
    random_hex = secrets.token_hex(8)
    file_name,filext = os.path.splitext(form_image.filename)
    image_name = random_hex + filext
    image_path = os.path.join(app.root_path,'static/images/profile_pix',image_name)
    form_image.save(image_path)
    return image_name


@app.route("/profile",methods=['GET','POST'])
@login_required
def profile():
    '''
    User profile page route
    '''
    form = UpdateProfile()
    projects = Post.query.filter_by(title=Post.title)
    if(form.image.data):
            image_file = save_image(form.image.data)
            current_user.profile_pic = image_file
    if(form.validate_on_submit()):
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.bio.data = current_user.bio
    profile_pic = url_for("static",filename="images/profile_pix/" + current_user.profile_pic)
    return render_template("profile.html",form=form,projects=projects,profile_pic=profile_pic)

@app.route("/register",methods=['GET','POST'])
def register():
    '''
    Registration route
    '''
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
    '''
    function for creating and posting a post
    '''
    form = PostForm()
    if(form.validate_on_submit()):
        project = Post(title=form.project_title.data,post=form.project_description.data,author=current_user)
        db.session.add(project)
        db.session.commit()
        return redirect("home")
    return render_template("createpost.html",title="New Post",form=form)

@app.route("/posts",methods=['GET'])
def posts():
    '''
    This function is used by the <iframe> tag to show posts
    '''
    projects = Post.query.all()
    profile_pic = url_for("static",filename="images/profile_pix/" + current_user.profile_pic)
    return render_template("posts.html",projects=projects,profile_pic=profile_pic)

@app.route("/sug_notifs",methods=['GET'])
def sug_notifs():
    '''
    This function is used by the <iframe> responsible for
    showing search results and suggestions and notifications
    '''
    return render_template("sug_results.html")