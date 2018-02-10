#!/usr/bin/python3
'''Base class model'''
import uuid
import datetime


class BaseModel():
    '''Base class of all models'''

    def __init__(self):
        '''Instance instantiation'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''__str__ representation'''
        string = '['+self.__class__.__name__+']'+' ('+self.id+') ' +\
                 str(self.__dict__)
        return string

    def save(self):
        '''Update updated_at time'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Serialize __dict__ and add class info'''
        j_dict = self.__dict__
        j_dict["__class__"] = self.__class__.__name__
        return j_dict

