from app import models
from app.extensions import db

def clear_db():
    art_items = models.User.query.all()
    for item in art_items:
        db.session.delete(item)
    db.session.commit()
