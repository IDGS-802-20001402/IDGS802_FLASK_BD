
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre', [validators.Length(min=4, max=25)])
    apellido = StringField('Apellido', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35), validators.Email()])