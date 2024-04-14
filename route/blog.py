from flask import request
from flask_accepts import accepts, responds
from flask_restx import Resource, Namespace
from service.blog_services import BlogServices
from utils.response import Responses

blog_api = Namespace("api")


@blog_api.route("/blog")
class Blog(Resource):
    def get(self):
        return {"Hello": "Nam"}

    # @accepts(query_params_schema=UserSchema, api=blog_api)
    # @responds(schema=UserSchemaResponse1, api=blog_api)
    def post(self):
        response = BlogServices.create_blog(request.json)
        return Responses.normal_response(response)

