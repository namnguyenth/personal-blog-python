from flask_restx import Resource, Namespace

ns = Namespace("api")


@ns.route("/category")
class Category(Resource):
    def get(self):
        return {"Hello": "Nam"}
    def post(self):
        return {"Hello": "Nam"}

@ns.route("/category/{id}")
class CategoryDetail(Resource):
    def get(self, id):
        return {"Hello": "Nam"}
    def post(self, id):
        return {"Hello": "Nam"}
    def put(self,id):
        return {"Method": "Deleted"}

