#!/usr/bin/python3
""" console.py
    The console of AirBnB project"""

import cmd
import re
import shlex
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
        args = shlex.split(line)

        if args == []:
            print("** class name missing **")
        else:
            try:
                dummy = storage.classes[args[0]]()
                print(dummy.id)
                storage.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance
            based on the class name and id. """
        args = shlex.split(line)

        if not args:
            print("** class name is missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            try:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                print(obj)
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name
            and id. """
        args = shlex.split(line)

        if not args:
            print("** class name is missing **")
        elif args[0] not in storage.classes:
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
        args = shlex.split(line)

        sobjlist = list()
        if not args:
            for obj in storage.all().values():
                sobjlist.append(str(obj))
        else:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    sobjlist.append(str(obj))

        print(sobjlist)

    def do_count(self, line):
        """ Prints all string """
        args = shlex.split(line)

        count = 0
        if not args:
            print("** class name missing **")
            return
        else:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    count += 1

        print(count)

    def do_update(self, line):
        """ updates an instance. """
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:

            if args[0] in storage.classes:
                try:
                    obj = storage.all()[f"{args[0]}.{args[1]}"]
                    if args[2] in obj.__class__.__dict__.keys():
                        arg_type = type(obj.__class__.__dict__[args[2]])
                        obj.__dict__[args[2]] = arg_type(args[3])
                    else:
                        obj.__dict__[args[2]] = args[3]
                    #storage.save()
                    obj.save()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def default(self, line):
        """ default """
        funcs = {"all": self.do_all, "show": self.do_show,
                 "update": self.do_update, "count": self.do_count,
                 "destroy": self.do_destroy}

        isfunc = re.search(r"^(.*)\.(.*)\((.*)\)", line)
        if isfunc and isfunc.group(2) in funcs:
            model = isfunc.group(1)
            func = isfunc.group(2)
            # Modifying args
            argslist = re.split(",", isfunc.group(3))
            newargs = list()
            for arg in argslist:
                newargs.append(arg.strip(" \""))
            line = model + " " + " ".join(newargs)
            funcs[func](line)
        else:
            print("*** Unkown syntax: {}".format(line))

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

    def help_count(self):
        """Help for count"""
        print('\n'.join(["Retrive the number of instances of a class"]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
