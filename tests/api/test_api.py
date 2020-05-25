import pytest
import requests

class TestAPI:
    url="https://pokeapi.co/api/v2/pokemon/bulbasaur/"

    def test_simple_search(self):
        response = requests.get(self.url)
        body = response.json()
        name = body["name"]
        assert name == "bulbasaur"
        
