#!/usr/bin/python3
"""
__init__ method for models directory.
Create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
