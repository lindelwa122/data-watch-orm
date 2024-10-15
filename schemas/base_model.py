from .manager import Manager

class BaseModel(type):
    """
    Metaclass for model classes. This allows for class-level customization.
    """
    def __new__(cls, name, bases, attrs):
        """
        Create a new class with the given name, bases, and attributes.
        
        :param name: Name of the class being created
        :param bases: Tuple of base classes
        :param attrs: Dictionary of class attributes
        :return: Newly created class
        """
        new_cls = super().__new__(cls, name, bases, attrs)
        return new_cls
    
class Model(metaclass=BaseModel):
    """
    Base class for all models in the ORM.
    """
    def __init__(self, db_path=':memory:'):
        """
        Initialize a new model instance.
        
        :param db_path: Path to the SQLite database file, defaults to in-memory database
        """
        self.manager = Manager(self.__class__, db_path)

    def __repr__(self):
        return self.__str__()
