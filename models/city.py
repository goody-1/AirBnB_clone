#!/usr/bin/python3
""" city.py
    The city class file """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    name = str()
    state_id = str()
