import pytest
import requests
import scripts
import string


# Test which checks length of array of all people with "count" field in response of simple get /people request
def test_length_array_people(sw_people):
    response_people = requests.get('https://swapi.dev/api/people/').json()
    assert len(sw_people) == response_people['count']


# Test which checks that names of all people are unique
def test_unique_names(sw_people):
    names = []
    for creature in sw_people:
        names.append(creature['name'])
    assert scripts.is_unique(names)


# Tests for validation that search for people is case insensitive
def test_case_insensitive_searching_1():
    search_input = 'Han'
    payload = {'search': search_input}
    payload_lower = {'search': search_input.lower()}
    assert requests.get('https://swapi.dev/api/people/', params=payload).json() == requests.get(
        'https://swapi.dev/api/people/', params=payload_lower).json()


def test_case_insensitive_searching_2():
    search_input = 'LUke'
    payload = {'search': search_input}
    payload_lower = {'search': search_input.lower()}
    assert requests.get('https://swapi.dev/api/people/', params=payload).json() == requests.get(
        'https://swapi.dev/api/people/', params=payload_lower).json()


# Test which will validate that there is no page with number 0 for people request
def test_null_page_doesnt_exist():
    payload = {'page': 0}
    status_code = requests.get('https://swapi.dev/api/people/', params=payload).status_code
    assert status_code == 404


# Parametrized test which will check that there are 3 Skywalker's, 1 Vader, 2 Darth's (using ?search)
@pytest.mark.parametrize('family, expected_result', [
    ('Skywalker', 3),
    ('Vader', 1),
    ('Darth', 2),
])
def test_count_of_families(family, expected_result):
    payload = {'search': family}
    assert requests.get('https://swapi.dev/api/people/', params=payload).json()['count'] == expected_result


# Test which will validate that all people objects contains required schema fields
def test_validate_people_fields(sw_people, sw_people_schema):
    for creature in sw_people:
        creature_fields = list(creature.keys())
        required_fields = sw_people_schema['required']
        for field in creature_fields:
            assert field in required_fields


# Test which will check that search for any char in English alphabet or
# any number from 0 to 9 will return number of results >0 except cases of
# search by 6, 9 and 0. It is not allowed to use loops inside the test body.
@pytest.mark.parametrize('case', list(string.ascii_lowercase) + list(range(0, 10)))
def test_check_char_and_number_search_more_than_zero(search_result, case):
    assert search_result(case)['count'] > 0
