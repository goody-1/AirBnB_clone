#!/usr/bin/python3

import json


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
        JSON file to instances. """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ returns the dictionay @__objects. """

        return (self.__objects)

    def new(self, obj):
        """ sets in @__objects the @obj with key:
            <obj class name>.id """

        name = str(type(obj).__name__) + "." + obj.id
        self.__objects.update({name: obj.to_dict()})

    def save(self):
        """ serializes @__objects to the JSON file """

        with open(self.__file_path, "w", encoding="utf-8") as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """ deserializes the JSON file to @__objects """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as fp:
                self.__objects = json.load(fp)
        except (IOError, json.JSONDecodeError):
            return
