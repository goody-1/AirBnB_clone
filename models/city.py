#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    name = str()
    state_id = str()
