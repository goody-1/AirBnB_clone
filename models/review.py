#!/usr/bin/pyhon3
""" review.py
    The review class file """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """

    place_id = str()
    user_id = str()
    text = str()
