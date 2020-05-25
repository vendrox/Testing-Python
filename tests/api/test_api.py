import pytest
import requests

class TestAPI:
    url_pokemon="https://pokeapi.co/api/v2/pokemon/bulbasaur/"
    url_type="https://pokeapi.co/api/v2/type/poison/"
    
    def test_simple_search(self):
        response = requests.get(self.url_pokemon)
        body = response.json()
        name = body["name"]
        assert name == "bulbasaur"

    def test_simple_type_search(self):
        response = requests.get(self.url_type)
        body = response.json()
        name = body["name"]
        assert name == "poison"
        
