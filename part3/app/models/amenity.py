from app.extensions import db

# Association table for many-to-many relationship between Place and Amenity

place_amenities = db.Table(
    'place_amenities',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True),
    extend_existing=True
)

class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    places = db.relationship('Place', secondary=place_amenities, back_populates='amenities')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
