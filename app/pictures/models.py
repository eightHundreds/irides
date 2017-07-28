from app.extensions import db


class UploadPic(db.Model):
    """UploadPic model """
    id = db.Column(db.Integer, primary_key=True)
    dsepriction= db.Column(db.String(5000), unique=True)
    address= db.Column(db.String(35), unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'))
    tags = db.relationship("PicTags",backref="UploadPic",lazy='dynamic')

    def to_json(self):
        """Returns a json representantion of the Pic.
        :returns: a json object.

        """

        json_pic={
            'id': str(self.id),
            'userid':self.user_id,
            'dsepriction':self.dsepriction,
            'adress': self.address,
            'tags': self.tags
        }

        return json_pic