#!/usr/bin/python3
""" Module for city class that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a Citys"""
    state_id = ""
    name = ""
