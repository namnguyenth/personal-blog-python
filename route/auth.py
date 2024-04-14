from flask import request
from flask_accepts import accepts, responds
from flask_restx import Resource, Namespace, reqparse

from schema.user_schema import UserSchemaResponse, UserSchema, UserSchemaResponse1
from service.user_services import UserServices
from utils.response import Responses

auth_api = Namespace("auth")


@auth_api.route("")
class Auth(Resource):
    def get(self):
        return UserServices.get()

    @accepts(query_params_schema=UserSchema, api=auth_api)
    @responds(schema=UserSchemaResponse1, api=auth_api)
    def post(self):
        response = UserServices.login(request.json)
        return Responses.normal_response(response)


@auth_api.route("/signup")
class Signup(Resource):

    @accepts(query_params_schema=UserSchema, api=auth_api)
    @responds(schema=UserSchemaResponse1, api=auth_api)
    def post(self):
        response = UserServices.signup(request.json)
        return Responses.normal_response(response)
