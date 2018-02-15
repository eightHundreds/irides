from passlib.apps import custom_app_context as pwd_context  # PassLib库对密码进行hash

from app import helpers
from app.extensions import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    avator = db.Column(db.String(35))
    email = db.Column(db.String(120), index=True)
    pictures = db.relationship('Picture', backref='user', lazy='dynamic')
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
            # 'pictures':self.pictures
        }
        return json_user


# 关联表tag_picture
relation = db.Table('tag_pic_relation',
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                    db.Column('picture_id', db.Integer, db.ForeignKey('pictures.id'))
                    )


class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    despriction = db.Column(db.String(5000), unique=True)
    address = db.Column(db.String(35), unique=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship(
        'Tag', secondary=relation, backref=db.backref('pictures', lazy='dynamic'))

    def to_json(self):
        templist = []
        for tag in self.tags:
            templist.append(tag.to_json())
        json_pic = {
            'id': str(self.id),
            'userid': self.userId,
            'dsepriction': self.despriction,
            'adress': self.address,
            'tags': templist
        }
        return json_pic


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))

    def to_json(self):
        json_tags = {
            'id': str(self.id),
            'tag': self.tag
        }
        return json_tags


class InitDataGenerator:
    @property
    def mock_user(self):
        if not self._user:
            self._user = User(
                username='admin',
                password=helpers.encrypt_password('password'),
                email="test@qq.com",
                avator="",
            )
        return self._user

    @property
    def mock_pictures(self):
        if not self._pictures:
            self._pictures = [
                Picture(despriction="test picture1",
                        address="https://s1.ax1x.com/2017/12/29/z06uF.png")
            ]
        return self._pictures

    def __init__(self):
        self._user=None
        self._pictures=None
        pass

    def init_all(self):
        self.init_user()
        self.init_picture()

    def init_picture(self):
        self.init_user()
        user = User.query.first()
        pics = self.mock_pictures.copy()
        for i in pics:
            i.userId = user.id
            db.session.add(i)
        db.session.commit()

    def init_user(self):
        if  User.query.filter(User.username == self.mock_user.username).first():
            return
        db.session.add(self.mock_user)
        db.session.commit()
