from app.extensions import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    places = db.relationship('Place', back_populates='owner', cascade='all, delete-orphan')
    reviews = db.relationship('Review', back_populates='user', cascade='all, delete-orphan')

    def set_password(self, plaintext_password):
        """Hash and store the password."""
        self.password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def verify_password(self, plaintext_password):
        """Check hashed password."""
        return bcrypt.check_password_hash(self.password, plaintext_password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }

from app.models.place import Place
from app.models.review import Review
