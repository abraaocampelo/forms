from flask_wtf import Form
from wtforms import StringField, validators
from wtforms.validators import DataRequired
from crypt import *


class LoginForm(Form):
    nome = StringField("nome", validators=[DataRequired()]) 
    email = StringField("email", validators=[DataRequired()]) 
    assunto = StringField("assunto", validators=[DataRequired()]) 
    mensagem = StringField("assunto", validators=[DataRequired()]) 
  

