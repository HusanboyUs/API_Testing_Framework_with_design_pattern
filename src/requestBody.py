from abc import ABC, abstractmethod
from typing import Dict, Self, Iterable,DefaultDict, Any


class AbstractRequestBody(ABC):

    @abstractmethod
    def serialize(self):
        pass


class RequestBody(AbstractRequestBody):
    
    def __init__(self, name:str, data:DefaultDict):
        self.name:str = name
        self.data:DefaultDict = data
    
    def serialize(self):
        return {
            "name": self.name,
            "data": self.data
        }


class RequestBodyBuilder:

    def __init__(self):
        self._name = None
        self._data:DefaultDict = {}

    def name(self, name:str) -> Self:
        if not isinstance(name, str):
            raise TypeError("String only please hehe!")
    
        self.name = name
        return self
    
    def add_data(self, key:str, value:Any) -> Self:
        if key not in self._data.keys():
            self._data[key] = value
            return self
    
        raise ValueError(f"{key} is already in the response data")
    
    def build(self):

        return RequestBody(
            name=self._name,
            data=self._data
        )


