from flask_restx import Resource, Namespace

category_api = Namespace("category")


@category_api.route("/<int:id>")
class Category(Resource):
    @category_api.doc(params={ 'id': 'Specify the Id associated with the person' })
    def get(self, id):
        data = {
            'id': id,
            'name': 'John Doe',
            'age': 30,
            'email': 'john@example.com'
        }
        return data
