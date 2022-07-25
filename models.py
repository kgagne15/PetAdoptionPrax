from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet model:
    id: PK int
    name: string, required
    species: string, required
    photo_url: string, optional
    age: int, optional
    notes: string, optional
    available: boolean, required, default True
    """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(500))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(500))
    available = db.Column(db.Boolean, nullable=False, default=True)