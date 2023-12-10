#!/usr/bin/python3
"""Defines unittests for console.py."""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import (
    HBNBCommand,
    validate_line,
    validate_attributes,
    parse_line
)


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Define setup"""
        self.cmd = HBNBCommand()

    def test_do_quit(self):
        """Test quit method"""
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_EOF(self):
        """Test for EOF"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.assertTrue(self.cmd.do_EOF(''))
            self.assertEqual(fake_output.getvalue().strip(), "")

    def test_validate_line(self):
        """Test for validate line"""
        available_classes = {"BaseModel", "User", "State",
                             "City", "Place", "Amenity", "Review"}
        self.assertTrue(validate_line("BaseModel.123", available_classes,
                        check_id=True))
        self.assertFalse(validate_line("", available_classes, check_id=True))

    def test_validate_attributes(self):
        """Test for validate attributes"""
        self.assertFalse(validate_attributes("show"))
        self.assertTrue(validate_attributes("show BaseModel"))

    def test_parse_line(self):
        """Test for oarse line method"""
        self.assertEqual(parse_line("example {text} [here]"),
                         ['example', 'text', 'here'])

    def test_do_create(self):
        """Test create"""
        with patch('builtins.print') as mock_print:
            self.cmd.do_create("BaseModel")
            self.assertTrue(mock_print.called)

    @patch('models.storage')
    def test_do_show(self, mock_storage):
        """Test show"""
        test_instance = BaseModel()
        test_instance.id = 'test_id'
        mock_storage.all.return_value = {'BaseModel.test_id': test_instance}
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.cmd.do_show("BaseModel test_id")
            self.assertEqual(fake_output.getvalue().strip(),
                             str(test_instance))


if __name__ == '__main__':
    unittest.main()
