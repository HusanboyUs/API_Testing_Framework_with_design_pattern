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
        print(result)
        # assert
        self.assertDictEqual(
            result.serialize(),
            expected
        ), "RequestBody builder did not built expected data"
        self.assertTrue(isinstance(RequestBody,result)), "Result is not instance of RequestBody"

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
        expected = {"name":"Macbook Pro", "data":""}
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
        expected = {"name":"", "data":{"color":"white"}}
        # assert
        self.assertDictEqual(
            result.serialize(),
            expected
        ), "Request builder did not return correct data"


if __name__ == "__main__":
    unittest.main()
