#!/usr/bin/python3
"""Storage module """
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, id(obj))
        FileStorage.__objects[key] = obj
    def save(self):
        with open( FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()} 
            json.dump(dict_obj, f)
    def reload(self):
        

