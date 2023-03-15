# SQLAlchemyPractice
Required Installations (inside venv):
- flask
- flask-sqlalchemy
- psycopg2-binary
- ipython

# Configuring SQL Application
Tells SQLAlchemy to communicate with postgresql using the database 'movies_example'
- app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'

# Working Outside of Application Context Error
- app.app_context().push()

# Steps to View Data in Database Using Terminal
Activate venv and start ipython
- %run app.py
- from sqlalchemy.sql import text
- movies = db.session.execute(text('SELECT * FROM movies'))
- list(movies)
- Will list all(*) data from movies table

# Create model and Add to Database
- Import model to app.py from models
- In ipython, create new model i.e. sumo = Pet(name='Sumo', species='dog', hunger=13)
- Add to database: db.session.add(sumo)
- Commit change to database: db.session.commit()

# Commit Multiple Models to Database
- In ipython:
- names = ['cricket', 'origami', 'abi']
- species = ['cat', 'cat', 'dog']
- zip(names, species)
- pets = [Pet(name=n, species=) for n, s in zip(names,species)]... where pets[0].name = 'cricket'
- db.session.add_all(pets)
- db.session.commit()
