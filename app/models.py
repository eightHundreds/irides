from passlib.apps import custom_app_context as pwd_context
from app.extensions import db

class User(db.Model):
    """User 模型 """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True)
    password_hash= db.Column(db.String(128))
    avator= db.Column(db.String(35), unique=True)
    email = db.Column(db.String(120), unique=True,index=True)
    uploadpic=db.relationship('UploadPic',backref='User',lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def to_json(self):
        json_user= {
            'id': str(self.id),
            'username': self.username,
            'avator': self.avator,
            'email':self.email,
            'Uploadpic':self.uploadpic
        }

        return json_user
class UploadPic(db.Model):
    """UploadPic 模型 """
    id = db.Column(db.Integer, primary_key=True)
    dsepriction= db.Column(db.String(5000), unique=True)
    address= db.Column(db.String(35), unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'))
    tags = db.relationship("PicTags",backref="UploadPic",lazy='dynamic')

    def to_json(self):
        json_pic={
            'id': str(self.id),
            'userid':self.user_id,
            'dsepriction':self.dsepriction,
            'adress': self.address,
            'tags': self.tags
        }

        return json_pic
class PicTags(db.Model):
    """PicTags 模型 """
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)
    pic_id = db.Column(db.Integer, db.ForeignKey('UploadPic.id'))

    def to_json(self):
        json_tags={
            'id': str(self.id),
            'tag': self.tag,
            'pic_id': self.pic_id
        }

        return json_tags