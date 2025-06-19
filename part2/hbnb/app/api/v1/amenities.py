from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity created')
    @api.response(400, 'Invalid input')
    def post(self):
        data = api.payload
        new_amenity = facade.create_amenity(data)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved')
    def get(self):
        amenities = facade.get_all_amenities()
        return [{'id': a.id, 'name': a.name} for a in amenities], 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity retrieved')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity updated')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        data = api.payload
        updated = facade.update_amenity(amenity_id, data)
        if not updated:
            return {'error': 'Amenity not found'}, 404
        return {'id': updated.id, 'name': updated.name}, 200
