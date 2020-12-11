from jinja2 import Template
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class  form(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])
    tocken = StringField('token', [validators.Length(min=6, max=100)])
    qnum = PasswordField('qnum', [validators.Length(min=6, max=10)])