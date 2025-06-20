from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns

api.add_namespace(users_ns)
api.add_namespace(places_ns)
