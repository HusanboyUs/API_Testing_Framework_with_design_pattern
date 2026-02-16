import pytest
from src import RequestClient, RequestBody, RequestBodyBuilder


class TestRestApi:

    @classmethod
    def setup_class(cls):
        cls.client = RequestClient()

    @pytest.mark.smoke
    def test_with_unrecognized_enpoints(self):
        # act
        response = self.client.get(endpoint="")
        #assert
        assert 401 == response.status_code
        assert "Unauthorized path" == response.json()["message"]

    def test_list_of_all_objects(self):
        # act
        response = self.client.get(endpoint="/objects")
        # assert
        assert 200 == response.status_code
        assert 13 == len(response.json())

    @pytest.mark.parametrize("ids",[
        (["1", "3", "5"]),
        (["7", "9", "13"]),
        (["12", "10", "2"]),
    ])
    def test_list_objects_by_ids(self, ids):
        #arrange
        result = "&".join(f"id={i}" for i in ids)
        #act
        response = self.client.get(endpoint="/objects?" + result)
        response_ids = (obj["id"] for obj in response.json())
        #arrange
        assert 200 == response.status_code
        assert set(response_ids) == set(ids)

    def test_list_objects_by_ids_without_ids(self):
        #act
        response = self.client.get(endpoint="/objects?id=")
        response.json()
        # assert
        assert 200 == response.status_code
        assert len(response.json()) == 0
        
    @pytest.mark.parametrize("ids",[
        (["99","1001"]),
        (["00990","99900"]),
    ])
    def test_list_objects_by_ids_with_nonexist_ids(self, ids):
        # arrange
        url_query = "&".join(f"id={i}" for i in ids)
        # act
        response = self.client.get(endpoint="/objects?" + url_query)
        # assert
        assert 200 == response.status_code
        assert 0 == len(response.json())
    
    def test_get_single_object(self):
        # act
        response = self.client.get(endpoint="/objects/7")
        res_obj = response.json()
        # assert
        assert res_obj["id"] == "7"
        assert res_obj["name"] == "Apple MacBook Pro 16"
        assert res_obj["data"]["year"] == 2019
        assert res_obj["data"]["CPU model"] == "Intel Core i9"
        assert res_obj["data"]["price"] == 1849.99
        assert res_obj["data"]["CPU model"] == "Intel Core i9"
        assert res_obj["data"]["Hard disk size"] == "1 TB"
    
    def test_get_single_object_with_nonexist_object(self):
        # arrange
        product_id = "999999"
        # act
        response = self.client.get(endpoint="/objects/" + product_id)
        # assert
        assert f"Object with id={product_id} was not found." == response.json()["error"]

    def test_post_new_object(self):
        # arrange
        laptop = (RequestBodyBuilder()
                .name("MacBook Pro 20")
                .add_data(key="color", value="black")
                .add_data(key="ram", value="16 GB")
                .add_data(key="os version", value="Ventura")
                .add_data(key="region", value="UK")
                .build()
            )
        # act
        response = self.client.post(endpoint="/objects", payload=laptop.serialize())
        response_body = response.json()
        # arrange
        assert 200 == response.status_code
        assert laptop.name == response_body["name"]
        assert laptop.data.get("color") == response_body["data"]["color"]
        assert laptop.data.get("ram") == response_body["data"]["ram"]
        assert laptop.data.get("os version") == response_body["data"]["os version"]
        assert laptop.data.get("region") == response_body["data"]["region"]

    def test_post_new_object_with_invalid_name(self):
        # arrange
        car = (RequestBodyBuilder()
                .add_data(key="color", value="black")
                .add_data(key="model", value="Tesla")
                .add_data(key="Milage", value="0")
                .build()
        )
        # act
        response = self.client.post(endpoint="/objects", payload=car.serialize())
        # assert
        assert 400 == response.status_code

    def test_post_object_without_name(self):
        # arrange
        iphone = (RequestBodyBuilder()
                .add_data(key="color", value="black")
                .add_data(key="model", value="Iphone 17 Pro")
                .add_data(key="used", value=False)
                .build()
        )
        # act
        response = self.client.post(endpoint="/objects", payload=iphone.serialize())
        response_body = response.json()
        # assert
        assert 200 == response.status_code
        assert "null" == response_body["name"]
        assert iphone.data.get("color") == response_body["data"]["color"]
        assert iphone.data.get("model") == response_body["data"]["model"]
        assert iphone.data.get("used") == response_body["data"]["cousedlor"]

    def test_post_object_without_data_and_only_with_name(self):
        # arrange
        music = (
            RequestBodyBuilder()
            .name("Faded by Alan Walker")
            .build()
        )
        # act
        response = self.client.post(endpoint="/objects", payload=music.serialize())
        response_body = response.json()
        # assert
        assert 200 == response.status_code
        assert music.name == response_body["name"]
        assert "null" == response_body["data"]



