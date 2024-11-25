#!/usr/bin/python3
"""
FileStorage class handlse serialization
and deserialization of objects to and frm JSON file
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Instance serialiation to JSON file and
    Deserialization for JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    __class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
    }

    def all(self):
        """
        dictionary __oblects
        """
        return self.__objects

    def new(self, obj):
        """
        args:
            obj: the object to store
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __object to JSON file
        """
        obj_dict = {key: obj.to_dict() for key, obj in self. __objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserilaization
        """
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
 
            for key, val in obj_dict.items():
                class_name = val["__class__"]
                self.__objects[key] = self.__class_dict[class_name](**val)

        except FileNotFoundError:
            pass
