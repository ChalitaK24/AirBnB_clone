#!/usr/bin/python3

import uuid

from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __ste__(self):
        return f"[{self.__class__.__name__}] (self.id) {seld.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] =self.updated_at.isoformat()

        return res
