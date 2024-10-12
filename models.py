"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        p = self
        return f"<Pet id={p.id}, name={p.first_name}, species={p.last_name}, hunger={p.image_url}>"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    first_name = db.Column(db.Text,
                     nullable = False)
    
    last_name = db.Column(db.Text, 
                        nullable = False)

    image_url = db.Column(db.Text, 
                       nullable = False)