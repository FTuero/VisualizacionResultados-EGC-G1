from ..model import *
from .. import app
from flask import render_template

@app.route('/visres')
def home():
    return render_template('result.html')