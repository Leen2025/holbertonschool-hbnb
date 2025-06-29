from flask_restx import Namespace, Resource


api = Namespace('reviews', description='Reviews operations')


@api.route('/')
class ReviewList(Resource):
    def get(self):
        """Retrieve a list of reviews"""
        return {
            "reviews": [
                {"id": 1, "user": "John", "comment": "Great place!"},
                {"id": 2, "user": "Sara", "comment": "Clean and cozy."}
            ]
        }
