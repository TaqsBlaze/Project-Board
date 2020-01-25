from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField,IntegerField,TextAreaField
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
    remember = BooleanField("Remeber me")
    submit = SubmitField('Login')



class UpdateProfile(FlaskForm):
    user_name = StringField("User name",validators=[DataRequired(),Length(min=1,max=30)])
    user_email = StringField("Email",validators=[DataRequired(),Length(min=4,max=120)])
    send = SubmitField("Update")
	
	
	
class PostForm(FlaskForm):
	project_title = StringField("Title",validators=[DataRequired(),Length(min=1,max=8)])
	project_description = TextAreaField("Descriptin",validators=[DataRequired(),Length(min=1,max=60)])
	submit = SubmitField("Post")