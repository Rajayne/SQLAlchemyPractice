from flask_sqlalchemy import SQLAlchemy

# DB MUST COME AFTER CONFIG
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS BELOW
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String,
                     nullable=False,
                     unique=True)
    
    species = db.Column(db.String(30), 
                        nullable=True)
    
    hunger = db.Column(db.Integer, 
                       nullable=False, 
                       default=20)

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()
    
    @classmethod
    def get_all_hungry(cls, hunger_level):
        return cls.query.filter(Pet.hunger >= hunger_level).all()

    def __repr__(self):
        p = self
        return f'<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>'
    
    def greet(self):
        return f'Hi, I am {self.name} the {self.species}.'
    
    def feed(self, amount=20):
        """Update hunger based off of amount"""
        self.hunger -= amount
        self.hunger = max(self.hunger, 0)