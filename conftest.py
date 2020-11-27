import pytest
import requests


@pytest.fixture
def sw_people():
    people = []
    payload = {'page': 1}
    response = requests.get('https://swapi.dev/api/people/', params=payload).json()
    while response['next'] is not None:
        response = requests.get('https://swapi.dev/api/people/', params=payload).json()
        res_people = response['results']
        people.extend(res_people)
        payload['page'] += 1
    return people
