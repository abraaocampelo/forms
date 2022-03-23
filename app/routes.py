from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato.html')
def contato():
    return render_template('contato.html')

@app.route('/features.html')
def features():
    return render_template('features.html')