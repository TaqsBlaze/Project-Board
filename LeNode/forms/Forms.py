from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField,SubmitField, BooleanField,IntegerField,TextAreaField,FileField
from wtforms.validators import DataRequired, Length,Email,EqualTo,ValidationError
from LeNode.Models.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    #number = IntegerField("Phone number",validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
      user = User.query.filter_by(username=username.data).first()
      if(user):
          raise ValidationError(f"{username.data} is already taken")

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if(email):
            raise ValidationError("that email is already taken")

class LoginForm(FlaskForm):
    #username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    user = StringField('User name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=8)])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')



class UpdateProfile(FlaskForm):
    username = StringField("User name",validators=[DataRequired(),Length(min=1,max=30)])
    bio = StringField("Bio",validators=[Length(min=4,max=120)])
    image = FileField("Update profile pic",validators=[FileAllowed(["png","jpg"])])
    send = SubmitField("Update")


    def validate_username(self,username):
        if(username.data != current_user.username):
            user = User.query.filter_by(username=username.data).first()
            if(user):
                raise ValidationError(f"{username.data} is already taken")

    def validate_bio(self,bio):
        if(bio.data != current_user.bio):
            bio = User.query.filter_by(bio=bio.data).first()
            if(bio):
                raise ValidationError("")

class PostForm(FlaskForm):
	project_title = StringField("Title",validators=[DataRequired(),Length(min=1,max=50)])
	project_description = TextAreaField("Descriptin",validators=[DataRequired(),Length(min=1,max=450)])
	submit = SubmitField("Post")

class Search(FlaskForm):
    search = StringField("Search",validators=[DataRequired()])
    submit = SubmitField("Search")