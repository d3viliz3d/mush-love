from flask import (
    Blueprint,
    render_template,
)

from ..app import mysql


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/register')
def signup():
    return render_template('register.html')


@auth.route('/logout')
def logout():
    return 'Logout'
