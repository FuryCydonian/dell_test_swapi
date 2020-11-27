import requests
import scripts


def test_length_array_people(sw_people):
    response_people = requests.get('https://swapi.dev/api/people/').json()
    assert len(sw_people) == response_people['count']


def test_unique_names(sw_people):
    names = []
    for creature in sw_people:
        names.append(creature['name'])
    assert scripts.is_unique(names)
