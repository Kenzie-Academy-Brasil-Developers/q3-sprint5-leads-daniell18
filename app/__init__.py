from flask import Flask
from app import routes

from app.config import database,migration
def create_app():
    app=Flask(__name__)
    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)
    return app