from app import helpers
from app import models
from app.extensions import db


def get_pictures():
    """Get all pictures"""
    pictures = models.Picture.query.filter_by().all()

    if not pictures:
        return {'no-data': ''}

    return {'success': [p.to_json() for p in pictures]}
