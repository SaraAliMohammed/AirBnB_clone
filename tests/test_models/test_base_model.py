"""Testing for the base_model module."""
import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """Test for BaseModel initialization."""
        base1 = BaseModel()
        base2_uuid = str(uuid.uuid4())
        base2 = BaseModel(id=base2_uuid, name="The weeknd", album="Trilogy")
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base2.id, str)
        self.assertEqual(base2_uuid, base2.id)
        self.assertEqual(base2.album, "Trilogy")
        self.assertEqual(base2.name, "The weeknd")
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertEqual(str(type(base1)),
                         "<class 'models.base_model.BaseModel'>")

    def test_attributes(self):
        """Test the initial attributes of BaseModel"""
        base = BaseModel()
        self.assertTrue(hasattr(base, 'id'))
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue(hasattr(base, 'updated_at'))
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertTrue(isinstance(base_dict, dict))
        self.assertIn('__class__', base_dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)

    def test_save_method(self):
        """Test save method"""
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(old_updated_at, base.updated_at)

    def test_save_storage(self):
        """Test save method of storage that is called from save()."""
        base = BaseModel()
        base.save()
        key = "{}.{}".format(type(base).__name__, base.id)
        dict = {key: base.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(len(file.read()), len(json.dumps(dict)))
            file.seek(0)
            self.assertEqual(json.load(file), dict)

    def test_save_method_no_args(self):
        """Test the save method with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        err_msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err_msg)

    def test_save_extra_args(self):
        """Test the  save method with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 100)
        err_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), err_msg)

    def test_str(self):
        """Test the str representation of the BaseModel"""
        base = BaseModel()
        string = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base.__str__(), string)


if __name__ == "__main__":
    unittest.main()
