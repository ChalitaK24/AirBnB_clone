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
        self._objects[key] = obj

    def reload_des(self):
        """
        deserilaization
        """
        try:

