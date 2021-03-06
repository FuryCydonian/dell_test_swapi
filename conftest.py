#
# Fixtures for tests
#
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


@pytest.fixture
def sw_people_schema():
    return requests.get('https://swapi.dev/api/people/schema').json()


@pytest.fixture
def search_result():
    def _search_result(request):
        payload = {'search': request}
        return requests.get('https://swapi.dev/api/people/', params=payload).json()
    return _search_result
