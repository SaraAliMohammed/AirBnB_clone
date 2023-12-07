#!/usr/bin/python3
"""Defines the console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    Attributes:
        prompt: Text of interactive prompt.
        __available_classes: Dictionary of available classes.
    """
    prompt = "(hbnb) "
    __available_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")
        print()

    def do_EOF(self, line):
        """exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in self.__available_classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        if not validate_line(line, self.__available_classes, check_id=True):
            return
        else:
            all_objects = storage.all()
            args = line.split()
            print(all_objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not validate_line(line, self.__available_classes, check_id=True):
            return
        else:
            all_objects = storage.all()
            args = line.split()
            del all_objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        all_objects = storage.all()
        if not line:
            print([str(v) for v in all_objects.values()])
        elif line.split()[0] not in self.__available_classes:
            print("** class doesn't exist **")
        else:
            class_name = line.split()[0]
            print([str(v) for v in all_objects.values()
                   if v.__class__.__name__ == class_name])

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if not validate_line(line, self.__available_classes, check_id=True):
            return
        elif not validate_attributes(line):
            return
        else:
            all_objects = storage.all()
            args = line.split()
            attr = args[2]
            value = args[3]
            key = "{}.{}".format(args[0], args[1])
            not_allowed = ("id", "created_at", "updated_at")
            if attr not in not_allowed:
                try:
                    if value.isdigit():
                        value = int(value)
                    elif float(value):
                        value = float(value)
                except ValueError:
                    pass
                class_dict = type(all_objects[key]).__dict__
                if attr in class_dict.keys():
                    try:
                        value = type(class_dict[attr])(value)
                    except Exception:
                        print("Entered wrong value type")
                        return
                setattr(all_objects[key], attr, value)
                storage.save()


def validate_line(line, available_classes, check_id=False):
    """Validates the arguments in the line"""
    if not line:
        print("** class name missing **")
        return
    args = line.split()
    if check_id:
        all_objects = storage.all()
    if args[0] not in available_classes:
        print("** class doesn't exist **")
        return False
    elif len(args) == 1 and check_id:
        print("** instance id missing **")
        return False
    elif check_id and "{}.{}".format(args[0], args[1]) not in all_objects:
        print("** no instance found **")
        return
    return True


def validate_attributes(line):
    """Validates the attributes in the line"""
    args = line.split()
    if len(args) == 2:
        print("** attribute name missing **")
        return False
    elif len(args) == 3:
        print("** value missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
