from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET','POST'])
def contato():
    form = LoginForm()
    if form.validate_on_submit():
        mensagem = flash('A mensagem foi enviada com sucesso. Nome: {}, e-mail: {}, assunto: {} e mensagem:{}'.format(
            form.nome.data, form.email.data, form.assunto.data, form.mensagem.data))
        return redirect('/index')
    return render_template('contato.html', form=form)
        

@app.route('/features')
def features():
    return render_template('features.html')



