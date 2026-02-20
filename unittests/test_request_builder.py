import unittest
from src.requestBody import RequestBody, AbstractRequestBody, RequestBodyBuilder



class TestRequestBody(unittest.TestCase):

    def test_request_body(self):
        # arrange
        rb = RequestBody(
            name="Iphone",
            data={"color":"black", "chip":"apple"}
        )
        expected = {
            "name":"Iphone",
            "data":{
                "color":"black",
                "chip":"apple"
            }
        }
        # act
        result = rb.serialize()
        # arrange
        self.assertDictEqual(
            result,
            expected
        ), "Class serialized unexpected object"
    
    def test_request_body_without_values(self):
        # arrange
        rb = RequestBody(
            name="",
            data=""
        )
        expected = {"name":'', "data":""}
        # act
        result = rb.serialize()
        # arrange
        self.assertDictEqual(
            result,
            expected
        ), "Request body did not return correct data"

    def test_request_body_with_null_values(self):
        # arrange
        rb = RequestBody(
            name=None,
            data=None
        )
        expected = {"name":None, "data":None}
        # act
        result = rb.serialize()
        # arrange
        self.assertDictEqual(
            result,
            expected
        ), "Request body did not handle null values"

    def test_request_body_with_updating_values(self):
        # arrange
        rb = RequestBody(
            name="Iphone 14",
            data={"chip":"apple"}
        )
        rb.name = "Iphone 14"
        rb.data["color"] = "white"
        expected = {"name":"Iphone 14", "data":{"chip":"apple","color":"white"}}
        # act
        result = rb.serialize()
        # assert
        self.assertDictEqual(
            result,
            expected
        ), "Request body did not change its values"


class TestRequestBuilder(unittest.TestCase):
    
    def test_request_builder(self):
        # arrange
        result = (
            RequestBodyBuilder()
            .name("Macbook Pro")
            .add_data("region","uk")
            .add_data("color", "white")
            .build()
        )
        expected = {"name":"Macbook Pro", "data":{
            "region":"uk",
            "color":"white"
        }}
        # assert
        self.assertDictEqual(
            result.serialize(),
            expected
        ), "RequestBody builder did not built expected data"
        self.assertTrue(isinstance(result, RequestBody)), "Result is not instance of RequestBody"

    def test_request_builder_with_wrong_name_instance(self):
        # assert
        with self.assertRaises(TypeError) as context:
            result = (
                RequestBodyBuilder()
                .name(None)
                .add_data("region","uk")
                .add_data("color", "white")
                .build()
            )
            self.assertEqual(str(context.exception), "Name type can be only string!")
    
    def test_request_builder_without_builder_method(self):
        # act
        result = (
            RequestBodyBuilder()
            .name("Iphone")
            .add_data("color","white")
        )
        not_expected = {"name":"Iphone", "data":{"color":"white"}}
        # assert
        self.assertNotEqual(
            result,
            not_expected
        )
    
    def test_request_builder_without_data_values(self):
        # act
        result = (
            RequestBodyBuilder()
            .name("Macbook Pro")
            .build()
        )
        expected = {"name":"Macbook Pro", "data":{}}
        # assert
        self.assertDictEqual(
            result.serialize(),
            expected
        ), "Request builder did not return correct data"

    def test_request_builder_without_name(self):
         # act
        result = (
            RequestBodyBuilder()
            .add_data("color","white")
            .build()
        )
        expected = {"name":None, "data":{"color":"white"}}
        # assert
        self.assertDictEqual(
            result.serialize(),
            expected
        ), "Request builder did not return correct data"
    
    def test_request_builder_with_big_data(self):
        # arrange
        result = (
            RequestBodyBuilder()
            .name("Copilot")
            .add_data("model","some-new-model")
            .add_data("year","2025")
            .add_data("owner","someonefromusa")
            .add_data("user","user")
            .add_data("limit",None)
            .add_data("token","")
            .add_data("used","false")
            .add_data("user-region","usa")
            .add_data("memory","enabled")
            .add_data("tracking",False)
            .add_data("vibe-coded",True)
            .add_data("random-amount", 500_500)
            .add_data("inner",{"name":"John"})
            .build()
        )

        expected = {
            "name":"Copilot",
            "data":{
                "model":"some-new-model",
                "year":"2025",
                "owner":"someonefromusa",
                "user":"user",
                "limit":None,
                "token":"",
                "used":"false",
                "user-region":"usa",
                "memory":"enabled",
                "tracking":False,
                "vibe-coded":True,
                "random-amount": 500_500,
                "inner":{"name":"John"}
            }
        }
        # act
        self.assertDictEqual(
            result.serialize(),
            expected
        )


if __name__ == "__main__":
    unittest.main()
