#!/usr/bin/python3
"""Defines the BaseModel Class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize object attributes.
        Attributes:
            id (string): assign with an uuid when an instance is created.
            created_at (datetime): the current datetime when an instance
                        is created.
            updated_at (datetime): assign with the current datetime
                        when an instance is created and it will be
                        updated every time you change your object.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    self.__dict__[k] = datetime.fromisoformat(v)
                elif k == "__class__":
                    continue
                elif k == "id":
                    self.__dict__[k] = str(v)
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """Print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                obj_dict[k] = v.isoformat()
            else:
                obj_dict[k] = v
        return obj_dict
