import uuid
from datetime import datetime


class BaseModel:
    """
    A class that contains the common attributes and method with class like User, Place....
    Public Attributes:
    id(string) - assign a unique id when an instance is created
    created_at(datetime) - assign the current date when instance is created
    updated_at(datetime) - assign the current date when instance is created and will be updated when the object change
    Methods:
    __str__: to print [<class name>] (<self,id>) <self.__dict__>
    save(self): update public instance attribute updated_at with current datetime
    to_dict(self): return a dictionary containing all k/v of __dict__ of the instance
    """

    def __init__(self):
        """Class initialized with public attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__>"""

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.update = datetime.now()
