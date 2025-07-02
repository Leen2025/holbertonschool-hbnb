# app/repositories/sqlalchemy_repository.py

from app.extensions import db

class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self):
        db.session.commit()

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()
