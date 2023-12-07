#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def setUp(self):
        self.city1 = City()
        self.city2 = City(**self.city1.to_dict())
        self.cit3 = City("welcome", "hi", "think")

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test the class attributes"""
        self.assertIsInstance(self.city1.name, str)
        self.assertEqual(self.city1.name, "")
        self.city1.name = "Alex"
        self.assertEqual(self.city1.name, "Alex")

    def test_initialization(self):
        """Test class instances"""
        self.assertIsInstance(self.city1.id, str)
        self.assertIsInstance(self.city1.created_at, datetime)
        self.assertIsInstance(self.city1.updated_at, datetime)
        self.assertEqual(self.city1.updated_at, self.city2.updated_at)

    def test_save_method(self):
        """Test the save method"""
        prev_update = self.city1.updated_at
        self.city1.save()
        self.assertNotEqual(self.city1.updated_at, prev_update)

    def test_todict(self):
        """Test the to_dict method"""
        city_dict = self.city2.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], type(self.city2).__name__)
        self.assertIn('created_at', city_dict.keys())
        self.assertIn('updated_at', city_dict.keys())
        self.assertNotEqual(self.city1, self.city2)


if __name__ == "__main__":
    unittest.main()
