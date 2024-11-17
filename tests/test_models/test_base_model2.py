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


if __name__ == "__main__":
    unittest.main()
