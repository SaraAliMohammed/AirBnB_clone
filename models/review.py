#!/usr/bin/python3
"""Defines the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class.
    Attributes:
        place_id (string): Place id.
        user_id (string): User id.
        text (string): Review text
    """
    place_id = ""
    user_id = ""
    text = ""
