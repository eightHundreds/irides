from app.extensions import db


class PicTags(db.Model):
    """PicTags model """
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def to_json2(self):
        """Returns a json representantion of the user.
        :returns: a json object.

        """

        return {
            'id': str(self.id),
            'username': self.username
        }
