from passlib.apps import custom_app_context as pwd_context
from app.extensions import db


class User(db.Model):
    """User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True)
    password_hash= db.Column(db.String(128))
    avator= db.Column(db.String(35), unique=True)
    email = db.Column(db.String(120), unique=True,index=True)
    uploadpic=db.relationship('UploadPic',backref='user',lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def to_json(self):
        """Returns a json representantion of the user.
        :returns: a json object.

        """
        json_user= {
            'id': str(self.id),
            'username': self.username,
            'avator': self.avator,
            'email':self.email,
            'Uploadpic':self.uploadpic
        }

        return json_user