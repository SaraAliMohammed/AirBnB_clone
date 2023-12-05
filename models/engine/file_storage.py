#!/usr/bin/python3
"""Defines A FileStorage Class
import json
from models.base_modele import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    Attributes:
        __file_path (string): path to the JSON file.
        __objects (dictionary): empty but will store all objects
                        by <class name>.id.
        classes_dict (dictionary): A dictionary of all the classes.
    """
    __file_path = "file.json"
    __objects = {}
    classes_dict = {"BaseModel": BaseModel}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (object): object to write.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps({k: v.to_dict()
                                   for k, v in self.__objects.items()}))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                for k, v in data.items():
                    new_obj = self.classes_dict[v['__class__']](**v)
                    self.__objects[k] = new_obj
        except Exception:
            pass
