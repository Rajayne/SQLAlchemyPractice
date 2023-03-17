"""Seed file to make sample data for pet_shop db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
sumo = Pet(name='Sumo', species='dog')
saydee = Pet(name='Saydee', species='dog')
vader = Pet(name='Vader', species='dog')
origami = Pet(name='Origami', species='cat')
cricket = Pet(name='Cricket', species='cat')

# Add and commit (save) to session
db.session.add(sumo)
db.session.add(saydee)
db.session.add(vader)
db.session.add(origami)
db.session.add(cricket)
db.session.commit()

