from app.extensions import db


class User(db.Model):
    """User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password= db.Column(db.String(300), unique=True)
    avator= db.Column(db.String(35), unique=True)
    email = db.Column(db.String(120), unique=True)
    uploadpic=db.relationship('UploadPic',backref='user',lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

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