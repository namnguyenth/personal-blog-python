from flask_restx import Resource, Namespace

blog_api = Namespace("api")


@blog_api.route("/blog")
class Blog(Resource):
    def get(self):
        return {"Hello": "Nam"}
    def post(self):
        return {"Hello": "Nam"}

