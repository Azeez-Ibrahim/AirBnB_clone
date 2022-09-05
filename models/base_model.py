#!/usr/bin/python3
"""Module for BaseModel class
   that defines all common attributes/methods
   for other classes
 """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """Initilazation of BaseModel instance
        Args:
            - *args: list of arguments
            - **kwargs: list of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a human-readable
        string representation of an instance
        """
        return "[{}] ({}) {}".\
               format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute
        with the current datetme
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance"""
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = type(self).__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict
