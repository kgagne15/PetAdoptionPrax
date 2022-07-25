
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField 

class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Pet Age")
    notes = StringField("Notes")