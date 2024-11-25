import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorageSave(unittest.TestCase):
    def test_save(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

