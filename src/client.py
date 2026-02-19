import requests
import json
from typing import Dict


class RequestClient:
    
    def __init__(self):
        self._base_url = "https://api.restful-api.dev"
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type":"application/json",
            "x-api-key":"
        })

    @property
    def baseurl(self):
        return self._base_url
    
    @baseurl.setter
    def baseurl(self, newurl:str):
        if not isinstance(newurl, str):
            raise TypeError("Url can be only string!")
        
    def get(self, endpoint:str):
        response = self.session.get(self.baseurl + endpoint)
        return response
    
    def post(self, endpoint:str, payload:dict):
        response = self.session.post(self.baseurl + endpoint, data=json.dumps(payload))
        return response
    
    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
    