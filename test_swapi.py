import requests
import pytest


@pytest.fixture
def sw_people():
    people = requests.get('https://swapi.dev/api/people/').json()['results']
    print(people)
    return people


