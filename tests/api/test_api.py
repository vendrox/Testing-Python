import pytest
from core.api.api_requests import APIRequests

<<<<<<< HEAD

=======
>>>>>>> f4a6bccfd756f021eebd7743f09c1ef9da85fd60
@pytest.mark.api
class TestAPI:

    expected_name = "bulbasaur"
    expected_type = "poison"

    def test_simple_search(self):
        body = APIRequests().pokemon_search(self.expected_name)
        name = body["name"]
        assert name == self.expected_name

    def test_simple_type_search(self):
        body = APIRequests().type_search(self.expected_type)
        name = body["name"]
        assert name == self.expected_type
