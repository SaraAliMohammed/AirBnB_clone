#!/usr/bin/python3
"""Defines the Place Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class.
    Attributes:
        city_id (string): City id.
        user_id (string): User id.
        name (string): Place name.
        description (string): Place description.
        number_rooms (integer): Place number of rooms.
        number_bathrooms (integer): Place number of pathrooms.
        max_guest (integer): Place maximum number of guests.
        price_by_night (integer): Place price by night.
        latitude (float): Place latitude value.
        longitude (float): Place longitude value.
        amenity_ids (list:string): Place list of amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
