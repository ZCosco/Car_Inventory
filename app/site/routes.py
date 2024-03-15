from flask import Blueprint, render_template
from models import Car

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@site.route('/profile')
def profile():
    return render_template('profile.html')