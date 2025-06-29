from flask_restx import Namespace, Resource

api = Namespace('amenities', description='Amenities operations')

@api.route('/')
class AmenityList(Resource):
    def get(self):
        return {'message': 'List of amenities'}
