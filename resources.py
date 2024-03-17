from flask_restx import Resource, Namespace

ns = Namespace("api2")


@ns.route("/locate")
class Locate(Resource):
    def get(self):
        return {"Hello": "Nam"}
    def post(self):
        return {"Hello": "Nam"}

@ns.route("/locate/{id}")
class Locate(Resource):
    def get(self, id):
        return {"Hello": "Nam"}
    def post(self, id):
        return {"Hello": "Nam"}
    def put(self,id):
        return {"Method": "Deleted"}

