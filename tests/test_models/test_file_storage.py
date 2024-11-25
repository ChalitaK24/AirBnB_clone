import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    def setUp(self):
        """Set up test case environment."""
        self.file_path = "file.json"
        self.storage = FileStorage()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_and_all(self):
        """Test new() and all() methods."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test save() and reload() methods."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Reload the objects
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_reload_no_file(self):
        """Test reload() when no file exists."""
        self.storage.reload()  # Should not raise an exception


if __name__ == "__main__":
    unittest.main()

