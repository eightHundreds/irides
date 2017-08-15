from app import helpers
from app import models
from app.extensions import db


def get_pictures():
    """Get all pictures"""
    pictures = models.Picture.query.filter_by().all()

    if not pictures:
        return {'no-data': ''}

    return {'success': [p.to_json() for p in pictures]}


def get_picture(picture_id):
    picture = models.Picture.query.filter_by(id=picture_id).first()

    if not picture:
        return {'no-data': ''}

    return {'success': [picture.to_json()]}
