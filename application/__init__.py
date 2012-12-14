from flask import Flask
from application.config import DevelopmentConfig
from application.config import ProductionConfig
from flask.ext.assets import Environment
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
import os


# setup Flask app
app = Flask(__name__)

# check APP_ENV environment variable and load the approprite config
if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# load assets plugin
assets = Environment(app)

# connect to the database
db = MongoEngine(app)

# load the login manager
login_manager = LoginManager()
login_manager.setup_app(app)


# login extension
@login_manager.user_loader
def load_user(email):
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return None


# import models
from application.models.user import User

# import forms
import application.forms.login

# import controllers
import application.controllers.site