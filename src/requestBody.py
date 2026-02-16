from abc import ABC, abstractmethod
from typing import Dict, Self, Iterable


class AbstractRequestBody(ABC):

    @abstractmethod
    def serialize(self):
        pass


class RequestBody(AbstractRequestBody):
    
    def __init__(self, name:str, price:float,year:int,cpu_model:str,hard_disk_size:str):
        self.name:str = name
        self.price:float = price
        self.year:int = year
        self.cpu_model:str = cpu_model
        self.hard_disk_size:str = hard_disk_size
    
    def serialize(self):
        return {
            "name": self.name,
            "data": {
                "year": self.year,
                "price": self.price,
                "CPU model": self.cpu_model,
                "Hard disk size": self.hard_disk_size,
            },
        }


class RequestBodyBuilder:

    def __init__(self):
        self._name = None
        self._year = None
        self._price = None
        self._cpu_model = None
        self._hard_disk_size = None

    def name(self, name:str) -> Self:
        if not isinstance(name, str):
            raise TypeError("String only please hehe!")
    
        self.name = name
        return self
    
    def year(self, year:int):
        self.year = year
        return self
    
    def pirce(self, price:float) -> Self:
        self.price = price
        return self
    
    def cpu_model(self, model:str):
        self.cpu_model = model
        return self
    
    def hard_disk_size(self, disksize:str):
        self.hard_disk_size = disksize
        return self
    
    def build(self):
        
        if self.name is None:
            raise ValueError("Object name is important")
        
        return RequestBody(
            name=self.name,
            year=self.year,
            price=self.price,
            cpu_model=self.cpu_model,
            hard_disk_size=self.hard_disk_size
        )
