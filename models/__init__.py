#!/usr/bin/python3

"""Initialization of models module"""
from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
