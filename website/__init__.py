# importing required modules from flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager


#creating database

db = SQLAlchemy()
DB_NAME = "database.db"

# defining a function for creating app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "w7g8&*F^&Scq67f^&c"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

# import relative modules inside same folder and they are for viewing web content
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth,url_prefix = "/")

    from .models import User, Post

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app





def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Database Created!")


