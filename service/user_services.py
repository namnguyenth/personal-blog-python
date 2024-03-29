from flask import jsonify

from model.models import User


class UserServices():
    def get():
        a = User.query.all()
        return jsonify(data=[a])


