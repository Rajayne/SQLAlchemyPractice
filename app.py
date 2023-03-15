from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__,template_folder='templates')
# Tells SQLAlchemy to communicate with postgresql using the database pet_shop
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop'
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Show home page"""
    return render_template('home.html')
