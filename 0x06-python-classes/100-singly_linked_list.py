#!/usr/bin/python3

"""module for a singly linked list"""


class Node(object):
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initilizes the node of a singly linked list
        Args:
            data - data part of a singly linked list
            next_node - contains value of the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data attribute
        Args:
            value - data value
        Raises:
            TypeError: if data is not an integer
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """Returns next node attribute
        Returns: next node value
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next node attribute
        Args:
            Value - next node value
        Raises:
            TypeError: if next node is not an object
        """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next node must be a Node object')

        self.__next_node = value


class SinglyLinkedList(object):
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes a Singly Linked List"""

        self.head = None

    def __str__(self):
        """Makes a list printable
        Returns: data in all the nodes"""

        printsll = ""
        location = self.head

        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node

        return printsll[:-1]

    def sorted_insert(self, value):
        """inserts a value in a sorted order
        Args:
            value - the value to be inserted in the node
        """

        new = Node(value)
        # linked list is empty
        if not self.head:
            self.head = new
            return
        # insert at the beginning of the list
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        location = self.head

        # traverse the linked list matching the data and value
        while location.next_node and location.next_node.data < value:
            location = location.next_node

        if location.next_node:
            # sort nodes
            new.next_node = location.next_node
        location.next_node = new
