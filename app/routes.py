from flask import render_template
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')