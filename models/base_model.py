#!/usr/bin/python3
"""
BaseModel class provides
common attr and mtds to be inherited by other classes
"""

import uuid

from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        new Base model instance initialize
        Args:
            *args: unused
            **kwargs: Key value pairs
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.fromisoformat(val)
                if key != "__class__":
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String representation of an instance

        Returns: str: Formatted string
        representation of the instance
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        `updated_at` with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing
        all keys/vals of the instance's __dict__
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()

        return res
