from flask_restx import Resource, Namespace

ns_blog = Namespace("api")


@ns_blog.route("/blog")
class Blog(Resource):
    def get(self):
        return {"Hello": "Nam"}
    def post(self):
        return {"Hello": "Nam"}
    def put(self):
        return {"Hello": "Nam"}
