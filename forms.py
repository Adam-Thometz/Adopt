"""Forms for Adopt"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pet to adoption database"""
    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired(message="Your animal is SOMETHING! What is it?")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional()])
    

class EditPetForm(FlaskForm):
    """Form for editing an existing pet"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional()])
    is_available = BooleanField("Available?")