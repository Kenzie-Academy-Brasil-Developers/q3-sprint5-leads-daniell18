from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from environs import Env
env=Env()
env.read_env()
db=SQLAlchemy()

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] =env("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.db=db
    from app.models.leads_models import Leads