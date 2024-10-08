from .manager import Manager

class BaseModel(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        new_cls.manager = Manager(new_cls)
        return new_cls
    
class Model(metaclass=BaseModel):
    def __repr__(self):
        return self.__str__()
