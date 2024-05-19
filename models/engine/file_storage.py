#!/usr/bin/python3
""" filestorage.py
    The FileStorage class file """

import json
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
        JSON file to instances. """

    __file_path = "file.json"
    __objects = dict()
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def all(self):
        """ returns the dictionay @__objects. """

        return (self.__objects)

    def new(self, obj):
        """ sets in @__objects the @obj with key:
            <obj class name>.id """

        name = str(type(obj).__name__) + "." + obj.id
        self.__objects[name] = obj

    def save(self):
        """ serializes @__objects to the JSON file """

        objdict = dict()

        for key, item in self.__objects.items():
            objdict[key] = item.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fp:
            json.dump(objdict, fp)

    def reload(self):
        """ deserializes the JSON file to @__objects """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as fp:
                objdict = json.load(fp)
                for key, value in objdict.items():
                    obj = self.classes[value['__class__']](**value)
                    self.__objects[key] = obj
        except (IOError, json.JSONDecodeError):
            return
