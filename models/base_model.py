#!/usr/bin/python3
"""
   BaseModel defines all common attributes/methods
   for other classes
 """
from datetime import datetime
import uuid
class BaseModel:
    """BAseModel class"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    def __init__(self, *args, **kwargs):
        
    def __str__(self):
        return pass
    def save(self):
        updated_at = datetime.now()
    def to_dict(self):
        return self.__dict__
