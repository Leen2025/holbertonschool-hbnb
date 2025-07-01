from app.extensions import db
from app import create_app
import os

app = create_app()

# Print the actual database URI being used by SQLAlchemy
print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully!")
