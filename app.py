from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# Tells Flask to use templates in templates folder
app = Flask(__name__,template_folder='templates')
# Tells SQLAlchemy to communicate with postgresql using the database movies_example
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
app.app_context().push()

db = SQLAlchemy()
db.app = app
db.init_app(app)

app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Show home page"""
    return render_template('home.html')
