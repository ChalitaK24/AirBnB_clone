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

    def test_idis_string(self):
        """
        Test if id is a string
        """

    def test_created_atis_datetime(self):
        """
        Test if created_at is a datetime object
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_atis_datetime(self):
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

    def test_save_update_updatedat(self):
        """
        save() updates updated_at
        """
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, prev_updated_at)
        self.assertGreater(self.model.updated_at, prev_updated_at)

    def test_to_dict_correct_keys(self):
        """
        to_dict contains the correct keys
        """
        model_dict = self.model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_to_dict_values(self):
        """
        to_dict values are properly formatted
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """
        initialization with kwargs
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(str(self.model), str(new_model))


if __name__ == "__main__":
    unittest.main()
