from app.extensions import db


class UploadPic(db.Model):
    """UploadPic model """
    Pic_Id = db.Column(db.Integer, primary_key=True)
    Pic_Dsepriction= db.Column(db.String(5000), unique=True)
    Pic_Address= db.Column(db.String(35), unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.User_Id'))
    tags = db.relationship("PicTags",backref="uploadpic")

    def Pics_Json(self):
        """Returns a json representantion of the Pic.
        :returns: a json object.

        """

        return {
            'id': str(self.Pic_Id),
            'Userid':self.user_id,
            'picname': self.Pic_Name,
            'dsepriction':self.Pic_Dsepriction,
            'adress': self.Pic_Address,
            'tags': self.tags
        }
