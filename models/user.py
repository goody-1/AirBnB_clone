#!/usr/bin/python3
""" user.py
    The user class file """

from models.base_model import BaseModel


class User(BaseModel):

    email = str()
    password = str()
    first_name = str()
    last_name = str()
