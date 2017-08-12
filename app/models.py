from passlib.apps import custom_app_context as pwd_context
from app.extensions import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password= db.Column(db.String(128))
    avator= db.Column(db.String(35))
    email = db.Column(db.String(120), index=True)
    picture = db.relationship('Picture', backref='user', lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def to_json(self):
        json_user= {
            'id': str(self.id),
            'username': self.username,
            'avator': self.avator,
            'email':self.email,
            #'picture':self.picture
        }
        return json_user

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    despriction = db.Column(db.String(5000), unique=True)
    address = db.Column(db.String(35), unique=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.id'))
    tags = db.relationship(
        'Tags', backref='picture', lazy='dynamic')

    def to_json(self):
        templist = []
        for tag in self.tags.all():
            templist.append(tag.to_json())
        json_pic={
            'id': str(self.id),
            'userid':self.userId,
            'dsepriction': self.despriction,
            'adress': self.address,
            'tags': templist
        }
        return json_pic

class Tags(db.Model):
    id = db .Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))
    picId = db.Column(db.Integer, db.ForeignKey('picture.id'))

    def to_json(self):
        json_tags = {
            'id': str(self.id),
            'tag': self.tag,
            'picId': self.picId
        }
        return json_tags
