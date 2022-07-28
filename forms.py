from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form to add new pet to database with name, species, photo_url, age, and notes as input data"""
    name = StringField("Pet Name", validators=[InputRequired(message="You must enter a name for your pet")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="You must enter a URL")])
    age = IntegerField("Pet Age", validators=[NumberRange(min=0, max=30, message="The age must be between 0 and 30")])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit an existing pet in database with option to edit photo_url, notes, and availability"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="You must enter a URL")])
    notes = StringField("Notes")
    available = BooleanField("Available")