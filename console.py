#!/urs/bin/python3

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNB cmd class """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}


    def do_EOF(self, line):
        """ Returns true to give a clean way to exit
            your interpreter """
        return (True)

    def do_quit(self, line):
        """ Returns true to give a clean way to exit
            your interpreter """
        return (True)

    def help_EOF(self):
        """Help for EOF"""
        print('\n'.join(["Returns true to give a clean way to",
                        "exit your interpreter."]))

    def help_quit(self):
        """Help for EOF"""
        print('\n'.join(["Returns true to give a clean way to",
                        "exit your interpreter."]))

    def emptyline(self):
        """ execute nothing when entering an empty line """
        pass

    def do_create(self, line):
        """ Creates a new instance """
        args = line.split()

        if args == []:
            print("** class name missing **")
        else:
            try:
                dummy = self.classes[args[0]]()
                print(dummy.id)
                storage.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance
            based on the class name and id. """
        args = line.split()

        if not args:
            print("** class name is missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            try:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                print(self.classes[args[0]](**obj))
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name
            and id. """
        args = line.split()

        if not args:
            print("** class name is missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            try:
                storage.all().pop(f"{args[0]}.{args[1]}")
                storage.save()
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string """
        args = line.split()

        sobjlist = list()
        if not args:
            for value in storage.all().values():
                obj = self.classes[value["__class__"]](**value)
                sobjlist.append(str(obj))
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for value in storage.all().values():
                if value["__class__"] == args[0]:
                    obj = self.classes[value["__class__"]](**value)
                    sobjlist.append(str(obj))

        print(sobjlist)

    def do_update(self, line):
        """ updates an instance. """
        args = line.split()

        argc = len(args)
        if argc == 0:
            print("** class name missing **")
        elif argc == 1:
            print("** instance id missing **")
        elif argc == 2:
            print("** attribute missing **")
        elif argc == 3:
            print("** value missing **")
        else:

            if args[0] in self.classes:
                try:
                    obj = storage.all()[f"{args[0]}.{args[1]}"]
                    obj.update({args[2]: args[3]})
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_create(self):
        """Help for create"""
        print('\n'.join(["Creats a new instance, saves it",
                        "(to the JSON file) an prints it."]))

    def help_show(self):
        """Help for show"""
        print('\n'.join(["Prints the string representation of an instance",
                        "based on the class name and id."]))

    def help_destroy(self):
        """Help for destroy"""
        print('\n'.join(["Deletes an instance based on the class name and",
                        "id."]))

    def help_all(self):
        """Help for all"""
        print('\n'.join(["Prints all string representaion of all instances",
                        "based or not on the class name."]))

    def help_update(self):
        """Help for update"""
        print('\n'.join(["Updates an instance bsed on the class name and id",
                        "by adding or updating attribute."]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
