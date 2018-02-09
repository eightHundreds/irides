from app import helpers
from app import models
from app.extensions import db


def get_pictures():
    """Get all pictures"""
    pictures = models.Picture.query.filter_by().all()

    if not pictures:
        return {'no-data': ''}

    return {'success': [p.to_json() for p in pictures]}


def get_specific_picture(pic_tag):
    """Get specific pictures"""

    pictures = models.Picture.query.filter(models.Picture.tags.any(tag=pic_tag)).all()
    if not pictures:
        return {'no-data': ''}

    return {'success': [picture.to_json() for picture in pictures]}
