from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import flask

app = flask.Flask(__name__)
import pymysql
mamager=Manager(app)
pymysql.install_as_MySQLdb()

app.config['SECRET_KEY'] ='you cannot guess it'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://irides:irides@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    """User model """
    User_Id = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(80), unique=True)
    User_Password= db.Column(db.String(300), unique=True)
    User_Avator= db.Column(db.String(35), unique=True)
    User_Email = db.Column(db.String(120), unique=True)
    uploadpic=db.relationship('UploadPic',backref='user',lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

class UploadPic(db.Model):
    """UploadPic model """
    Pic_Id = db.Column(db.Integer, primary_key=True)
    Pic_Dsepriction= db.Column(db.String(5000), unique=True)
    Pic_Address= db.Column(db.String(35), unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.User_Id'))
    tags = db.relationship("PicTags",backref="uploadpic")

class PicTags(db.Model):
    """PicTags model """
    Tag_Id = db.Column(db.Integer, primary_key=True)
    Tag = db.Column(db.String(50), unique=True)

picture = db.Table('picture',
    db.Column('UploadPic.Pic_Id', db.Integer, db.ForeignKey('UploadPic.Pic_Id')),  
    db.Column('PicTags.Tag_Id', db.Integer, db.ForeignKey('PicTags.Tag_Id'))  
)  

if __name__=='__main__':
    mamager.run()