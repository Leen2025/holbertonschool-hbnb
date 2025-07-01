# run.py

from app import create_app
from app.extensions import db
from app.models import user, place, amenity, review  # make sure all models are imported

app = create_app()

with app.app_context():
    db.create_all()  # This creates all tables if they don't exist

if __name__ == '__main__':
    app.run(debug=True)
