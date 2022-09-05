#!/usr/bin/python3
"""Module for file storage class that serializes instances
   to a JSON file and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Class representing file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dict_obj = json.load(f)
            from models.base_model import BaseModel

            for k, v in dict_obj.items():
                if v["__class__"] == "BaseModel":
                    FileStorage.__objects[k] = BaseModel(**v)
