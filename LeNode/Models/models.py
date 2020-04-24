from datetime import datetime
from LeNode import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    profile_pic = db.Column(db.String(20),unique=False,default='default.png')
    password = db.Column(db.String(60),nullable=False)
    bio = db.Column(db.String(120),unique=False)
    notifications = db.Column(db.Integer,primary_key = False,unique = False,default = 0)
    level = db.Column(db.Integer,primary_key = False,unique = False,default = 0)
    notifs = db.relationship('Notifications',backref='author',lazy=True)
    posts = db.relationship('Post',backref='author',lazy=True)
    file = db.relationship('Files',backref='author',lazy=True)
    media = db.relationship('Media',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_pic}','{self.notifications}','{self.level}')"



class Post(db.Model):
     id = db.Column(db.Integer,primary_key = True)
     title = db.Column(db.String(200),nullable=False)
     votes = db.Column(db.Integer,primary_key=False,unique=False, default = 0)
     date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
     post = db.Column(db.Text(),nullable=False)
     comments = db.relationship('Comments',backref='author',lazy=True)
     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

     def __repr__(self):
         return f"Post('{self.title}','{self.post}','{self.votes}')"
     
     
class Comments(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.Text(),nullable=False)
    user = db.Column(db.Text(),nullable=False)
    comment_datetime = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
         return f"Comments('{self.comment}','{self.comment_datetime}')"

class Notifications(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text(),nullable=False)
    _from = db.Column(db.Text(),nullable=False)
    time = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
         return f"Notifications('{self.title}','{self._from}','{self.time}')"
     
class Files(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    file = db.Column(db.String(30),unique=False,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Files('name_string:{self.file}','file_id:{self.id}','user_id:{self.user_id})"
class Media(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    images = db.Column(db.String(30),unique=False,nullable=True)
    videos = db.Column(db.String(30),unique=False,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Media('{self.images}','{self.videos}')"