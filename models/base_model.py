#!/usr/bin/python3
"""
   BaseModel defines all common attributes/methods
   for other classes
 """
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = type(self).__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict
