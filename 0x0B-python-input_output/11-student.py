#!/usr/bin/python3
"""Module contains a student class"""


class Student:
    """This defines the student class with some attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:

            return self.__dict__
        else:
            dic = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dic[attr] = getattr(self, attr)
            return (dic)

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
