import pytest
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


def test_case_insensitive_searching():
    search_input = 'Han'
    payload = {'search': search_input}
    payload_lower = {'search': search_input.lower()}
    assert requests.get('https://swapi.dev/api/people/', params=payload).json() == requests.get(
        'https://swapi.dev/api/people/', params=payload_lower).json()


def test_null_page_doesnt_exist():
    payload = {'page': 0}
    status_code = requests.get('https://swapi.dev/api/people/', params=payload).status_code
    assert status_code == 404


@pytest.mark.parametrize('family, expected_result', [
    ('Skywalker', 3),
    ('Vader', 1),
    ('Darth', 2),
])
def test_count_of_families(family, expected_result):
    payload = {'search': family}
    assert requests.get('https://swapi.dev/api/people/', params=payload).json()['count'] == expected_result


def test_validate_people_fields(sw_people, sw_people_schema):
    for creature in sw_people:
        creature_fields = list(creature.keys())
        required_fields = sw_people_schema['required']
        for field in creature_fields:
            assert field in required_fields
