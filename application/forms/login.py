from flask.ext.wtf import Form
from flask.ext.wtf import TextField
from flask.ext.wtf import PasswordField
from flask.ext.wtf import Required


class LoginForm(Form):
    email = TextField('email', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
