#!/usr/bin/python3
"""
   BaseModel defines all common attributes/methods
   for other classes
 """
from datetime import datetime
import uuid
class BaseModel:
    """BAseModel class"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return pass
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        return self.__dict__
