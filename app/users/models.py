from app.extensions import db


class User(db.Model):
    """User model """
    User_Id = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(80), unique=True)
    User_Password= db.Column(db.String(300), unique=True)
    User_Avator= db.Column(db.String(35), unique=True)
    User_Email = db.Column(db.String(120), unique=True)
    uploadpic=db.relationship('UploadPic',backref='user',lazy='dynamic')
    """lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据"""

    def Users_Json(self):
        """Returns a json representantion of the user.
        :returns: a json object.

        """

        return {
            'id': str(self.User_Id),
            'username': self.User_Name,
            'avator': self.User_Avator,
            'email':self.User_Email,
            'Uploadpic':self.uploadpic
        }
