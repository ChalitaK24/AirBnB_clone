#!/usr/bin/python3

import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
