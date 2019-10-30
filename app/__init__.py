from flask import Flask
# import flask_login
from flask_cors import CORS
# from flask_login import LoginManager
from werkzeug.utils import secure_filename
import config

from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager


app = Flask(__name__)
CORS(app)


# Configure app
app.config['SECRET_KEY'] = config.SECRET_KEY

# # login_manager = LoginManager()
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)
# login = LoginManager(app)
# login.login_view = 'login'


from app import routes, models
