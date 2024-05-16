#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ AirBnb's base model that defines all attributes
        and methods. """

    def __init__(self, *args, **kwargs):
        """ initializiation function """
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            kwargs.pop("__class__")
            self.__dict__.update(**kwargs)

            # Converting strings data to datatime format.
            cr, up = kwargs["created_at"], kwargs["updated_at"]
            cr = datetime.strptime(cr, format("%Y-%m-%dT%H:%M:%S.%f"))
            up = datetime.strptime(up, format("%Y-%m-%dT%H:%M:%S.%f"))
            self.__dict__.update({"created_at": cr, "updated_at": up})


    def __str__(self):
        """ prints data about an instance:
            format:
            [<class name>] (<self.id>) <self.__dict__>
            """
        form = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

        return (form)

    def save(self):
        """ updates the @update_at public intance attribute
            with the current date time. """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance. """

        instance_dict = dict()
        instance_dict.update(**self.__dict__)
        instance_dict.update({"__class__": type(self).__name__,
                              "created_at": self.created_at.isoformat(),
                              "updated_at": self.created_at.isoformat()})
        

        return (instance_dict)
