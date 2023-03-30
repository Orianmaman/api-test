import pytest
import requests

class TestApi:
    def test_1(self):
        url = 'https://fruityvice.com/api/fruit/banana'

        response = requests.get(url)
        assert 400 > response.status_code >= 200



    def test_2(self):
        url = 'https://fruityvice.com/api/fruit/kiwi'
        response = requests.get(url)
        dict1 = response.json()
        expected = 66
        actual = dict1['id']
        assert actual == expected




