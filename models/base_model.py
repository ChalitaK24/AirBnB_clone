#!/usr/bin/python3

import uuid


class Basemodel:
    def __init__(slef, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4()):wq

