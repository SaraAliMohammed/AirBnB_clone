#!/usr/bin/python3
"""Defines the User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that contains all user information.
    Attributes:
        email (string): User email.
        password (string): User password.
        first_name (string): User first name.
        last_name (string): User last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
