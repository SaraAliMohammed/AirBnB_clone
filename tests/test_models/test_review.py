#!/usr/bin/python3
"""Tests for the review module."""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test for the Review class."""

    def setUp(self):
        """Define Setup"""
        self.review1 = Review()
        self.review2 = Review("welcome", "hi", "think")
        self.review3 = Review(**self.review1.to_dict())

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_class_attributes(self):
        """Test the class attributes"""
        key = f"{type(self.review1).__name__}.{self.review1.id}"
        self.assertIsInstance(self.review1.text, str)
        self.assertIsInstance(self.review1.user_id, str)
        self.assertIsInstance(self.review1.place_id, str)
        self.assertEqual(self.review1.text, "")

    def test_initialization(self):
        """Test Review instances"""
        self.assertIsInstance(self.review1.id, str)
        self.assertIsInstance(self.review1.created_at, datetime)
        self.assertIsInstance(self.review1.updated_at, datetime)
        self.assertEqual(self.review1.updated_at, self.review3.updated_at)

    def test_str_method(self):
        """Test the str method"""
        rev = self.review1
        r = f"[{type(rev).__name__}] ({rev.id}) {rev.__dict__}"
        self.assertEqual(rev.__str__(), r)

    def test_save_method(self):
        """Test the save method"""
        prev_update = self.review1.updated_at
        self.review1.save()
        self.assertNotEqual(self.review1.updated_at, prev_update)

    def test_todict_method(self):
        """Test the to_dict method"""
        review_dict = self.review3.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], type(self.review3).__name__)
        self.assertIn('created_at', review_dict.keys())
        self.assertIn('updated_at', review_dict.keys())
        self.assertNotEqual(self.review1, self.review3)


if __name__ == "__main__":
    unittest.main()
