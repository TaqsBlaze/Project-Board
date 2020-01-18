from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length,Email,EqualTo,ValidationError
from LeNode.Models.models import User
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    #number = IntegerField("Phone number",validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=8)])
    conferm_password = PasswordField('Conferm Password',validators=[DataRequired(),EqualTo('password')])
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
    remender = BooleanField("Remeber me")
    submit = SubmitField('Login')



class PostForm(FlaskForm):
    post = StringField("enter text",validators=[DataRequired(),Length(min=1,max=30)])
    send = SubmitField("Send")
