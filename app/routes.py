from crypt import methods
from app import app
from flask import render_template
from crypt import methods
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST','GET'])
def contato():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.nome.data)
        print(form.email.data)
    return render_template('contato.html', form = form)


@app.route('/features')
def features():
    return render_template('features.html')


