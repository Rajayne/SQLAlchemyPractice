from flask_sqlalchemy import SQLAlchemy

# DB MUST COME AFTER CONFIG
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS BELOW