import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class
    """

    def setUp(self):
        """
        setup testcase environment
        """

    def test_instance_frm_kwargs(self):
        """
        instance initialization with kwargs
        """
        obj_dict = self.model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertNotEqual(id(new_model), id(self.model))


if __name__ == "__main__":
    unittest.main()
