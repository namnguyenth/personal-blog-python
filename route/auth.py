from flask_restx import Resource, Namespace

from service.user_services import UserServices

auth_api = Namespace("auth")


@auth_api.route("/auth")
class Auth(Resource):
    def get(self):
        return UserServices.get()
