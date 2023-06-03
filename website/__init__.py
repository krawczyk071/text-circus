import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)

    # /// = relative path, //// = absolute path
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    db.create_all(app=app)
    print('Created Database!')
