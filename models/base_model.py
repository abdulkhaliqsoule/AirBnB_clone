#!/usr/bin/python3
"""BaseModel that defines all common attributes and
    methods for all the other classes"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    A class that contains the common attributes
    and method with class like User, Place....
    """

    def __init__(self):
        """Class initialized with public attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of base model"""
        return "[{}] {} {}".format(self.__class__.__name__,
                                   self.id, self.__dict__)

    def save(self):
        """updates updated_at with current datetime"""
        self.updated = datetime.now()

    def to_dict(self):
        """returns a dictionary of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
