from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa 
from ..models import Usuario
from app import db

class LoginForm(FlaskForm):
    nome = StringField('Nome', validators = [DataRequired()])
    senha = PasswordField('Senha', validators = [DataRequired()])
    lembre_me = BooleanField('Lembre de mim')
    enviar = SubmitField('Enviar')

class RegistrationForm(FlaskForm):
    nome = StringField('Nome', validators = [DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    cpf = StringField('CPF', validators = [DataRequired()])
    data_nascimento = DateField('Data de nascimento', format = '%d/%m/%Y')
    telefone = StringField('Telefone', validators = [DataRequired()])
    genero = RadioField('Gênero', choices = ['Feminino', 'Masculino', 'Transgênero', 'Não-binário', 'Outro'])
    tipo_usuario = RadioField('Tipo de usuário', choices = ['Empresa', 'Admin', 'Professor'])
    senha = PasswordField('Senha', validators = [DataRequired()])
    senha2 = PasswordField('Confirme sua senha', validators = [DataRequired(), EqualTo('senha')])
    enviar = SubmitField('Enviar')

    def validar_usuario(self, nome):
        usuario = db.session.scalar(sa.select(Usuario).where(Usuario.nome == nome.data)).first()
        if usuario is not None:
            return ValidationError('Esse nome já está sendo usado.')

    def validar_email(self, email):
        email = db.session.scalar(sa.select(Usuario).where(Usuario.email == email.data))
        if email is not None:
            return ValidationError('Esse email já está sendo usado.')