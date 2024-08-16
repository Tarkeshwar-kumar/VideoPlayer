
from flask import request, jsonify
from flask_restx import Resource
from app.models.db import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class Register(Resource):
    def post(self):
        user = User(
            id=request.json["id"],
            username=request.json["username"],
            email=request.json["email"],
            password=request.json["password"]
        )
        db.session.add(user)
        db.session.commit()
        return {"status": "success"}

class Login(Resource):
    def get(self):
        user = db.session.execute(db.select(User.id).filter_by(username=request.json["username"], password=request.json["password"]))
        response = user.fetchone()
        access_token = create_access_token(identity=request.json["username"])
        return {"status": "success", "user_id": response[0], "token": access_token}
    
class GetUser(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        return {"status": "success", "user": current_user}