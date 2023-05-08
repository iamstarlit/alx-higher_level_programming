#!/usr/bin/python3
"""base.py model contains the base class."""

import json
import csv
import turtle


class Base(object):
    """Defines the Base class.

    Attributes:
        __nb_objects (int): Number of objects/instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance of base class.

        Args:
            id (int): id parameter
        """
        # Check if ID is not an int.
        if id is not None and not isinstance(id, int):
            raise TypeError("ID must be an integer.")

        # Check if id is None
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            # Check if ID is negative
            if id <= 0:
                raise ValueError("ID must be a non-zero  positive integer.")
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary into JSON string.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            list: list of dictinaries (json string)
        """
        # check if list is None
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save object in a file.

        Args:
           list_objs (list): list of objects
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)

        # Create json strings from dictinaries
        list_dict = []

        for obj in list_objs:
            list_dict.append(obj.to_dictionary())

        # Write to json file
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """JSON string into list of dictinaries.

        Args:
            json_string (json): JSON string

        Returns:
            list: list of dictinaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of the class from a dictionary of attributes.

        Args:
            **dictionary (dict): A dictionary of key-value pairs representing
                the attributes of the new instance.

        Returns:
            A new instance of the class, with attributes set according to
            the provided dictionary.
        """
        # If the dictionary is not empty, create a new instance of the class
        if dictionary:
            if cls.__name__ == "Rectangle":
                # If the class is Rectangle, create a new instance
                # with width and height set to 1
                new_instance = cls(1, 1)
            else:
                # Otherwise, create a new instance with size set to 1
                new_instance = cls(1)

            # Update the attributes of the new instance
            # with the values in the dictionary
            new_instance.update(**dictionary)

            # Return the new instance
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file and instantiate them as class objects.

        Returns:
            list: A list of instantiated class objects.

        """
        # Define the filename using the class name
        filename = "{}.json".format(cls.__name__)

        try:
            # Attempt to open the file and read its contents
            with open(filename) as f:
                # Load the JSON data as a list of dictionaries
                # using your custom from_json_string() method
                json_data = cls.from_json_string(f.read())

                # Create a list of class objects instantiated
                # from the dictionaries
                objects = [cls.create(**d) for d in json_data]
                return objects

        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the list of objects to a CSV file.

        Args:
            list_objs (list): list of objects
        """
        if list_objs is None:
            list_objs = []

        # Create file name.
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        # Append rows to a list
        csv_rows = []

        for obj in list_objs:
            dict_obj = obj.to_dictionary()
            row = [dict_obj[key] for key in list_keys]
            csv_rows.append(row)

        # Write to a CSV file.
        with open(filename, 'w', newline='') as csv_obj:
            # Create Writer object
            writer = csv.writer(csv_obj)
            writer.writerows(csv_rows)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file and instantiate them as class objs.

        Returns:
            list: A list of instantiated class objects
        """
        # Define filename using the class name
        filename = "{}.csv".format(cls.__name__)

        try:
            # Attempt to open the file and read its contents
            with open(filename) as csvfile:
                if cls.__name__ == "Rectangle":
                    list_keys = ['id', 'width', 'height', 'x', 'y']
                else:
                    list_keys = ['id', 'size', 'x', 'y']

                # Use DictReader to read CSV file as list of dictionaries
                list_dicts = csv.DictReader(csvfile, fieldnames=list_keys)

                # Convert the values in the dictionaries to integers
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]

                # Create a list of instantiated objects from dictionary.
                objects = [cls.create(**d) for d in list_dicts]
                return objects

        except FileNotFoundError:
            # return empty list if file does not exist
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and Squares.

        Args:
            list_rectangles (list): list of Rectangles
            list_squares (list): list of Squares
        """
        t = turtle.Turtle()
        t.screen.bgcolor(1,1,1)

        t.color(0,0,0)
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()

            t.begin_fill()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            
            t.end_fill()
            t.hideturtle()

        t.color(1,0.1,0.8)
        for sqr in list_squares:
            t.showturtle()
            t.up()
            t.goto(sqr.x, sqr.y)
            t.down()

            t.begin_fill()
            for _ in range(4):
                t.forward(sqr.size)
                t.left(90)

            t.end_fill()
            t.hideturtle()

        turtle.exitonclick()
