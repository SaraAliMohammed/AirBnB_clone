#!/usr/bin/python3
"""Tests for the state module."""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test State class."""

    def setUp(self):
        self.state1 = State()
        self.state2 = State("welcome", "hi", "think")
        self.state3 = State(**self.state1.to_dict())

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_parameters(self):
        """Test class parameters"""
        key = f"{type(self.state1).__name__}.{self.state1.id}"
        self.assertIsInstance(self.state1.name, str)
        self.assertEqual(self.state2.name, "")
        self.state1.name = "Chicago"
        self.assertEqual(self.state1.name, "Chicago")
        self.assertIn(key, storage.all())

    def test_initialization(self):
        """Test State instances"""
        self.assertIsInstance(self.state1.id, str)
        self.assertIsInstance(self.state1.created_at, datetime)
        self.assertIsInstance(self.state1.updated_at, datetime)
        self.assertEqual(self.state1.updated_at, self.state3.updated_at)

    def test_str_method(self):
        """Test the str method"""
        st = self.state1
        text = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
        self.assertEqual(self.state1.__str__(), text)

    def test_save_method(self):
        """Test the save method"""
        prev_update = self.state1.updated_at
        self.state1.save()
        self.assertNotEqual(self.state1.updated_at, prev_update)

    def test_todict_method(self):
        """Test the to_dict method"""
        state_dict = self.state2.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], type(self.state3).__name__)
        self.assertIn('created_at', state_dict.keys())
        self.assertIn('updated_at', state_dict.keys())
        self.assertNotEqual(self.state1, self.state3)


if __name__ == "__main__":
    unittest.main()
