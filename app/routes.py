from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo = 'Home')

@app.route('/contato', methods=['GET','POST'])
def contato():
    form = LoginForm()
    if form.validate_on_submit():
        print  ("Chegou aqui")
        mensagem = flash('A mensagem foi enviada com sucesso.')
    return render_template('contato.html', form=form, titulo = 'Contato')
        

@app.route('/sobre')
def features():
    return render_template('sobre.html', titulo = 'Sobre')



