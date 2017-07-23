from .users.models import *
from .tags.models import *
from .pictures.models import *
#当导入该文件后,如from app import models,可以通过models.Users去引用模型类,相当于把分布到多个文件夹下model都放到models下

picture = db.Table('picture',
    db.Column('UploadPic.Pic_Id', db.Integer, db.ForeignKey('UploadPic.Pic_Id')),  
    db.Column('PicTags.Tag_Id', db.Integer, db.ForeignKey('PicTags.Tag_Id'))  
)  