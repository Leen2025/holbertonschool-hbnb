# app/repositories/in_memory_repository.py

import uuid

class InMemoryRepository:
    def __init__(self):
        # Dictionary to store data: {id: object}
        self._storage = {}

    def add(self, obj):
        """Add a new object and assign a unique ID"""
        if not hasattr(obj, 'id') or not obj.id:
            obj.id = str(uuid.uuid4())
        self._storage[obj.id] = obj
        return obj

    def get(self, obj_id):
        """Retrieve an object by its ID"""
        return self._storage.get(obj_id)

    def get_all(self):
        """Retrieve all stored objects"""
        return list(self._storage.values())

    def get_by_attribute(self, attr_name, attr_value):
        """Find an object by a specific attribute value"""
        for obj in self._storage.values():
            if hasattr(obj, attr_name) and getattr(obj, attr_name) == attr_value:
                return obj
        return None
