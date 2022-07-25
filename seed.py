"""Seed file to make sample data for db."""

from models import db, Pet
from app import app


#Create all tables
db.drop_all()
db.create_all()

dog = Pet(name="Rocky", species="dog", photo_url="https://static.inspiremore.com/wp-content/uploads/2020/11/16113321/Grumpy-Dog-Challenge-24.jpg",
age=2, notes="Rocky has the best smile", available=True)
cat = Pet(name="Kiki", species="cat", photo_url="https://preview.redd.it/7cu5lub5okl21.jpg?auto=webp&s=5ad2cf86d114e14c63cbd7bfc57124f17abbc880",
age=5, notes="Kiki is a menace", available=True)
porcupine = Pet(name="Spikey", species="porcupine", photo_url="http://cincinnatizoo.org/system/assets/uploads/2013/03/porcupine.jpg",
age=3, notes="Spikey likes hugs", available=True)

db.session.add_all([dog, cat, porcupine])
db.session.commit()