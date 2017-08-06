from app import models
from app.extensions import db
from flask import current_app
def clear_db():
    if current_app.config['SQLALCHEMY_DATABASE_URI'].find('memory')!=-1:
        db.create_all()
    art_items = models.User.query.all()
    for item in art_items:
        db.session.delete(item)
    db.session.commit()
