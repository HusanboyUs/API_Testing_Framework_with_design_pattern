from .client import RequestClient
from .requestBody import RequestBodyBuilder, RequestBody


class Application:

    def __init__(self):
        self.client = RequestClient()

    def list_of_all_objects(self):
        request = self.client.get()

