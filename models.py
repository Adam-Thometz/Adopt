from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMG_URL = 'https://peoplewithpets.com/wp-content/uploads/2019/11/people-with-pets-no-image-available.jpg'
# For styling purposes, above img is 900 x 600

db = SQLAlchemy()

def connect_db(app):
    """Connect db to app. Call in app.py"""
    
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets up for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)

    def image_url(self):
        """Return image for pet, whether there's a url for the photo or not"""

        return self.photo_url or DEFAULT_IMG_URL