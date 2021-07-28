# importing required modules from flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# defining a function for creating app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "w7g8&*F^&Scq67f^&c"

# import relative modules inside same folder and they are for viewing web content
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth,url_prefix = "/")

    return app
