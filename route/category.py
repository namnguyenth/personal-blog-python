from flask_restx import Resource, Namespace

category_api = Namespace("category")


@category_api.route("/")
class Category(Resource):
    def get(self):
        return {"Hello": "Nam"}
    def post(self):
        return {"Hello": "Nam"}