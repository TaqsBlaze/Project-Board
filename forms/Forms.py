from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length,Email,EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	number = IntegerField("Phone number",validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=8)])
	conferm_password = PasswordField('Conferm Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	#username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
	user = StringField('User name',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=8)])
	remender = BooleanField("Remeber me")
	submit = SubmitField('Login')



class Post(FlaskForm):
	message = StringField("Message",validators=[DataRequired(),Length(min=1,max=30)])
	send = SubmitField("Send")
