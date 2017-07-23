from app.extensions import db


class PicTags(db.Model):
    """PicTags model """
    Tag_Id = db.Column(db.Integer, primary_key=True)
    Tag = db.Column(db.String(50), unique=True)

    def Tags_Json(self):
        """Returns a json representantion of the tags.
        :returns: a json object.

        """

        return {
            'id': str(self.Tag_Id),
            'tag': self.Tag
        }