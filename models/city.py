#!/usr/bin/python3
"""Defines the City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the city class.
    Attributes:
        state_id (string): State id.
        name (string): City name.
    """
    state_id = ""
    name = ""
