#!/urs/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


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
        args = line.split()
        classes = ["BaseModel"]

        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            dummy = BaseModel()
            print(dummy.id)

    def do_show(self, line):
        args = line.split()
        classes = ["BaseModel"]

        if not args:
            print("** class name is missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            try:
                print(storage.all()[f"BaseModel.{args[1]}"])
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")


    def help_create(self):
        """Help for create"""
        print('\n'.join(["Creats a new instance, saves it",
                        "(to the JSON file) an prints it."]))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
