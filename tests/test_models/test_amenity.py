#!/usr/bin/python3
"""Unit tests for the amenity module."""
import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_parameters(self):
        """Test class attributes"""

        amen1 = Amenity()
        amen2 = Amenity(**amen1.to_dict())
        amen3 = Amenity("welcome", "hi", "test")

        t = f"{type(amen1).__name__}.{amen1.id}"
        self.assertIsInstance(amen1.name, str)
        self.assertIn(t, storage.all())
        self.assertEqual(amen3.name, "")

    def test_initialization(self):
        """Test new instances"""
        amen1 = Amenity()
        amen2 = Amenity(**amen1.to_dict())
        self.assertIsInstance(amen1.id, str)
        self.assertIsInstance(amen1.created_at, datetime)
        self.assertIsInstance(amen1.updated_at, datetime)
        self.assertEqual(amen1.updated_at, amen2.updated_at)

    def test_str(self):
        """Test str method"""
        amen1 = Amenity()
        string = f"[{type(amen1).__name__}] ({amen1.id}) {amen1.__dict__}"
        self.assertEqual(amen1.__str__(), string)

    def test_save(self):
        """Test save method"""
        amen1 = Amenity()
        prev_update = amen1.updated_at
        amen1.save()
        self.assertNotEqual(amen1.updated_at, prev_update)

    def test_todict(self):
        """Test dict method"""
        amen1 = Amenity()
        amen2 = Amenity(**amen1.to_dict())
        amen2_dict = amen2.to_dict()
        self.assertIsInstance(amen2_dict, dict)
        self.assertEqual(amen2_dict['__class__'], type(amen2).__name__)
        self.assertIn('created_at', amen2_dict.keys())
        self.assertIn('updated_at', amen2_dict.keys())
        self.assertNotEqual(amen1, amen2)


if __name__ == "__main__":
    unittest.main()
