import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects(self):
        storage = FileStorage()
        self.assertEqual(FileStorage._FileStorage__objects, {})

