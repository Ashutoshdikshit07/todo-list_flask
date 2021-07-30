from flask import Blueprint
from flask import blueprint, render_template
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')