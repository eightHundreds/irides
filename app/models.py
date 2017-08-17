from passlib.apps import custom_app_context as pwd_context  # PassLib库对密码进行hash
from datetime import datetime
from app import helpers
from app.extensions import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    avator = db.Column(db.String(35))
    email = db.Column(db.String(120), index=True)
    picture = db.relationship('Picture', backref='user', lazy='dynamic')
    commnet = db.relationship('Comments', backref='user', lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def to_json(self):
        json_user = {
            'id': str(self.id),
            'username': self.username,
            'avator': self.avator,
            'email': self.email,
            # 'picture':self.picture,
            # 'comment':self.comment
        }
        return json_user


# 关联表
relation = db.Table('relation',
                    db.Column('tags_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
                    db.Column('picture_id', db.Integer, db.ForeignKey('picture.id'), primary_key=True)
                    )


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    despriction = db.Column(db.String(5000), unique=True)
    address = db.Column(db.String(35), unique=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.id'))
    tags = db.relationship(
        'Tags', secondary=relation, backref=db.backref('picture', lazy='dynamic'))
    commnet = db.relationship('Comments', backref='picture', lazy='dynamic')

    def to_json(self):
        taglist = []
        for tag in self.tags:
            taglist.append(tag.to_json)
        commlist = []
        for comment in self.comments:
            commlist.append(comment.to_json)
        json_pic = {
            'id': str(self.id),
            'userid': self.userId,
            'dsepriction': self.despriction,
            'adress': self.address,
            'tags': taglist,
            'comments': commlist
        }
        return json_pic


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))

    @property
    def to_json(self):
        json_tags = {
            'id': str(self.id),
            'tag': self.tag
        }
        return json_tags

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    userId = db.Column(db.Integer, db.ForeignKey('User.id'))
    picId = db.Column(db.Integer, db.ForeignKey('picture.id'))

    def to_json(self):
        json_comments = {
            'id': str(self.id),
            'body': self.body,
            'timestamp': self.timestamp,
            'userId': self.userId,
            'picId': self.picId
        }
        return json_comments
