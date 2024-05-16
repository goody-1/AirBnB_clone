#!/urs/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNB cmd class """

    prompt = "(hbnb) "
    classes = ["BaseModel"]

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
            match args[0]:
                case "BaseModel":
                    dummy = BaseModel()
                    print(dummy.id)
                    storage.save()
                case _:
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
                print(BaseModel(**obj))
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

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
                sobjlist.append(str(BaseModel(**value)))
        else:
            match args[0]:
                case "BaseModel":
                    for value in storage.all().values():
                        if value["__class__"] == args[0]:
                            sobjlist.append(str(BaseModel(**value)))
                case "User":
                    for value in storage.all().values():
                        if value["__class__"] == args[0]:
                            sobjlist.append(str(User(**value)))
                case _:
                    print("** class doesn't exist **")
                    return

        print(sobjlist)



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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
