from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized review attempt')
    @jwt_required()
    def post(self):
        """Create a new review (authenticated users only)"""
        try:
            review_data = api.payload
            current_user_id = get_jwt_identity()
            review_data['user_id'] = current_user_id

            place = facade.get_place(review_data['place_id'])
            if not place:
                return {"error": "Place not found"}, 404

            if str(place.owner_id) == str(current_user_id):
                return {"error": "You cannot review your own place"}, 403

            if facade.user_already_reviewed_place(current_user_id, place.id):
                return {"error": "You already reviewed this place"}, 403

            review = facade.create_review(review_data)
            return review, 201
        except Exception as e:
            return {"error": str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Get all reviews (public)"""
        try:
            reviews = facade.get_all_reviews()
            return reviews, 200
        except Exception as e:
            return {"error": str(e)}, 400


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get a review by ID (public)"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized')
    @jwt_required()
    def put(self, review_id):
        """Update a review (only by its owner)"""
        current_user_id = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        if str(review['user_id']) != str(current_user_id):
            return {"error": "Unauthorized"}, 403

        try:
            updated = facade.update_review(review_id, api.payload)
            return {"message": "Review updated successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review (only by its owner)"""
        current_user_id = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        if str(review['user_id']) != str(current_user_id):
            return {"error": "Unauthorized"}, 403

        deleted = facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place (public)"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        try:
            reviews = facade.get_reviews_by_place(place_id)
            return reviews, 200
        except Exception as e:
            return {"error": str(e)}, 400
