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

