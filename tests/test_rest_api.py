import pytest
from .base_test import BaseTest
from src import RequestClient, RequestBody


class TestRestApi(BaseTest):

    @classmethod
    def setup_class(cls):
        cls.client = RequestClient()

    # @pytest.mark.smoke
    # def test_application_is_up_and_runnnig(self):
    #     # act
    #     response = self.client.get("/")
    #     # assert
    #     self.assertEqual(200, response.status_code, msg="Application did not return 200 status code!")

    @pytest.mark.smoke
    def test_with_unrecognized_enpoints(self):
        # act
        response = self.client.get(endpoint="")
        response_body =response.json()
        #assert
        self.assertEqual(401, response.status_code)
        self.assertEqual("Unauthorized path", response_body["message"])

    def test_list_of_all_objects(self):
        # act
        response = self.client.get(endpoint="/objects")
        response_body = response.json()
        # assert
        self.assertEqual(200, response.status_code)
        self.assertEqual(13, len(response_body), msg="Items in response is bigger or less than 13")

    @pytest.mark.parametrize("ids",[
        ()
    ])
    def test_list_objects_by_ids(self):
        #act
        response = self.client.get(endpoint="objects?")
        response_body = response.json()
        #arrange
        self.assertEqual(200, response.status_code)



    