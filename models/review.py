#!/usr/bin/python3
""" Module for review class that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review"""
    place_id = ""
    user_id = ""
    text = ""
