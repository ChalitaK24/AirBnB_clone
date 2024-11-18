#!/usr/bin/python3
"""
FileStorage class handlse serialization and deserialization of objects to and frm JSON file
"""

import json


class FileStorage:
    """
    Instance serialiation to JSON file and
    Deserialization for JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all_d(self):
        """
        dictionary __oblects
        """
        return self.__objects

    def new_o(self, obj):
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
        obj_dict = {key: obj.to_dict() for key, obj in self. _objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload_des(self):
        """
        deserilaization
        """
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
            from models.base_model import BaseModel
            for key, val in obj_dict.items():
                class_name = val["__class__"]
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass

