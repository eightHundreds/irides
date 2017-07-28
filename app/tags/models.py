from app.extensions import db


class PicTags(db.Model):
    """PicTags model """
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)
    pic_id = db.Column(db.Integer, db.ForeignKey('UploadPic.id'))

    def to_json(self):
        """Returns a json representantion of the tags.
        :returns: a json object.

        """
        json_tags={
            'id': str(self.id),
            'tag': self.tag,
            'pic_id': self.pic_id
        }

        return json_tags