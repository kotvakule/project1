from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField('Название товара:')
    description = StringField('Описание товара:')
    price = StringField('Цена товара:')
    submit = SubmitField('Добавить товар')

class LoginForm2(FlaskForm):
    name = StringField('Введите имя:')
    surname = StringField('Введите фамилию:')
    login = StringField('Введите логин:')
    phone = StringField('Введите номер телефона:')
    submit = SubmitField('Добавить пользователя')
