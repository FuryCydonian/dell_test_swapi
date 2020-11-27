import requests
import pytest


@pytest.fixture
def sw_people():
    people = requests.get('https://swapi.dev/api/people/').json()['results']
    print(people)
    return people


def test_length_array_people(sw_people):
    response_people = requests.get('https://swapi.dev/api/people/').json()
    assert len(sw_people) == response_people['count']
