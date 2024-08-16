from flask import Flask
from flask_restx import Api
from app.routes.routes import Register, Login, GetUser
from app.models.db import db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask("authentication")
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videoplayer.db'
    app.config["JWT_SECRET_KEY"] = "weatherisgoodtoday"
    db.init_app(app)
    jwt = JWTManager(app)
    api.add_resource(Register, "/register")
    api.add_resource(Login, "/login")
    api.add_resource(GetUser, "/me")
    return app