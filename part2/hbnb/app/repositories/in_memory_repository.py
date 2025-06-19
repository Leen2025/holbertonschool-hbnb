# app/repositories/in_memory_repository.py

import uuid

class InMemoryRepository:
    def __init__(self):
        self.objects = {}
    def add(self, obj):
        self.objects[obj.id] = obj
    def get(self, obj_id):
        return self.objects.get(obj_id)
    def get_by_attribute(self, attr, value):
        for obj in self.objects.values():
            if getattr(obj, attr, None) == value:
                return obj
        return None
    def get_all(self):
        return list(self.objects.values())
    def update(self, obj_id, obj):
        self.objects[obj_id] = obj