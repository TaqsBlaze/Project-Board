from datetime import datetime
from LeNode import db


def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    profile_pic = db.Column(db.String(20),unique=False,default='default.png')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

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