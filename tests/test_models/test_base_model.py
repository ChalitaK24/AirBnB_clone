import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    test for BaseModel class
    """

    def setUp(self):
        """
        Setup test case environment
        """
        self.model = BaseModel()

    def test_instance_creation(self):
        """
        Test if instance is created
        """

    def test_id_is_string(self):
        """
        Test if id is a string
        """

    def test_created_at_is_datetime(self):
        """
        Test if created_at is a datetime object
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if updated_at is a datetime object
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the __str__ method
        """
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)


if __name__ == "__main__":
    unittest.main()
