
from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField 
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="You must enter a name for your pet")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="You must enter a URL")])
    age = IntegerField("Pet Age", validators=[NumberRange(min=0, max=30, message="The age must be between 0 and 30")])
    notes = StringField("Notes")