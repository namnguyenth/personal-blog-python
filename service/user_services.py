import datetime

from flask import jsonify
from flask_restx import abort
from http import HTTPStatus

from extensions import db
from model.models import User
from utils.common import Common


class UserServices():
    def get():
        a = User.query.all()
        return jsonify(data=[{
            "hello": 1
        }])

    def login(request):
        user = request.get("user_name")
        pwd = request.get("password")

        query = User.query.filter_by(user_name=user, password=pwd)
        account = query.first()
        if not account:
            raise abort(code=HTTPStatus.BAD_REQUEST, message="Incorrect username or password.")
        response = [
            {
                "uuid": account.user_name,
                "user_name": account.user_name,
            }
        ]
        return response

    def signup(request):
        user = request.get("user_name")
        pwd = request.get("password")

        query = User.query.filter_by(user_name=user)
        account = query.first()
        if account:
            raise abort(code=HTTPStatus.BAD_REQUEST, message="Username is already exist.")

        new_user = User(
            uuid=Common.uuid_generator(),
            user_name=user,
            password=pwd,
            created_date=datetime.datetime.utcnow(),
            created_by="40e6215d-b5c6-4896-987c-f30f3678f600",
        )

        db.session.add(new_user)
        db.session.commit()
        db.session.flush()

        response = [
            {
                "uuid": new_user.uuid,
                "user_name": new_user.user_name,
                "created_date": new_user.created_date,
                "created_by": new_user.created_by
            }
        ]

        return response
