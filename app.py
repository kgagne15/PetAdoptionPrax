from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petsareawesome"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_all_pets():
    """Route that lists all pets in the database and their availability"""
    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add')
def add_pet():
    """Route to get form to add new pet to database"""
    form = AddPetForm()
    return render_template('add_pet_form.html', form=form)

@app.route('/add', methods=["POST"])
def post_pet():
    """Route to submit new pet to database"""
    form = AddPetForm()
    if form.validate_on_submit(): 
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data or None
        notes = form.notes.data or None
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=True)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{name} is now listed for adoption!")
        return redirect('/add')
    else: 
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:id>')
def edit_pet_form(id):
    """Route to edit existing pet in database"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    return render_template('edit_pet_form.html', form=form, pet=pet)

@app.route('/<int:id>', methods=["POST"])
def submit_pet_edit(id):
    """Route to submit edits of existing pet in database"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet.id}')
    else: 
        return render_template('edit_pet_form.html', form=form, pet=pet)