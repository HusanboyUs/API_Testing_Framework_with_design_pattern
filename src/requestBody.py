from abc import ABC, abstractmethod
from typing import Dict, Self, Any


class AbstractRequestBody(ABC):

    @abstractmethod
    def serialize(self):
        pass


class RequestBody(AbstractRequestBody):
    
    def __init__(self, name:str, data:Dict):
        self.name:str = name
        self.data:Dict = data
    
    def serialize(self):
        """
        Returns as json/dict type
        """
        return {
            "name": self.name,
            "data": self.data
        }


class RequestBodyBuilder:

    def __init__(self):
        self._name = None
        self._data:Dict = {}

    def name(self, name:str) -> Self:
        """
        Adds name to request body
        
        :param name:str = name of the object
        :rtype: Self
        """
        if not isinstance(name, str):
            raise TypeError("Name type can be only string!")
    
        self._name = name
        return self
    
    def add_data(self, key:str, value:Any) -> Self:
        """
        Add extra data to request body
        
        :param key: Object key
        :type key: Object value
        :rtype: Self
        Example:
            car, "black"
        """
        if key not in self._data.keys():
            self._data[key] = value
            return self
    
        raise ValueError(f"{key} is already in the response data")
    
    def build(self):
        """
        Builds given object and returns as Request instance
        """
        return RequestBody(
            name=self._name,
            data=self._data
        )
