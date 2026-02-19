import pytest
from src import RequestClient, RequestBodyBuilder, RequestBody


class TestUserSuccessStory:

    @classmethod
    def setup_class(cls):
        cls.client = RequestClient()
        cls.product = (
            RequestBodyBuilder()
            .name("Macbook Air")
            .add_data("color", "black")
            .add_data("ram", "16GB")
            .add_data("chip","Apple M4")
            .build()
        )
        cls.response = None

    def a_test_create_object_in_application(self):
        # act
        response = self.client.post(endpoint="/objects", payload=self.product.serialize())
        self.response = response
        # assert
        assert 200 == response.status_code

    def b_test_search_for_product(self):
        # arrange
        response = self.response.json()
        # act
        response = self.client.get(endpoint=f"/objects/{response["id"]}")
        response_body = response.json()
        # assert
        assert 200 == response.status_code
        assert self.product.name == response_body["name"]
        assert self.product.data["color"] == response_body["data"]["color"]
        assert self.product.data["ram"] == response_body["data"]["ram"]
        assert self.product.data["chip"] == response_body["data"]["chip"]
    
    