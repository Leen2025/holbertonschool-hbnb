from flask_restx import Namespace, Resource

api = Namespace('places', description='Places operations')

@api.route('/')
class PlaceList(Resource):
    def get(self):
        return {'message': 'List of places'}
