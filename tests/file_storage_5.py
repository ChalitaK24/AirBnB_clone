import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorageReload(unittest.TestCase):
    def test_reload(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

