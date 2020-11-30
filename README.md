# Test the Star Wars API

## Clone and run
- Clone repository
- Change directory `cd <repository_name>`
- Install poetry (a tool for dependency management and packaging in Python.): `pip install poetry`
- Install dependencies: `poetry install`
- Install **make**. `<package_manager> install make` or any other way for your system (without **make** look for below)
- activate virtual environment `source ./<env_name>/bin/activate` for Linux or `<env_name>\Scripts\activate.bat` for Windows
- Run test file: `make` or `make test`. Or without **make**: `pytest test_swapi.py -vv --html=report.html`
- Result is in console and in report.html file


## Test tasks
Write a suite for the Star Wars world. Service endpoints (only GET requests):


- Use the service described on site https://swapi.dev/ as target service under the test.
- full documentation: https://swapi.dev/documentation  (please read it at least till Encoding block)
- base url for all requests = https://swapi.dev/api/

Use Python and libraries: _pytest_, _requests_ 

Feel free to use any other libraries in addition to these but pytest must be used as test framework and requests library for http requests.

Note: If you don't know about fixtures in pytest please read pytest docs about that first

Project structure is up to you: it can be just single file with all code inside it or a set of files, but execution command must execute all tests at once.

 Tasks (1-8 are mandatory, 9 - it is better to do it but not very critical, 10 – more complex and will add some additional points for you, 11-12 are abstract tasks and up to you):


1. create fixture which will return the array of all people
2. create test which checks length of array of all people with "count" field in response of simple get /people request
3. create test which checks that names of all people are unique
4. create a few tests for validation that search for people is case insensitive
5. create test which will validate that there is no page with number 0 for people request
6. reate parametrized test which will check that there are 3 Skywalker's, 1 Vader, 2 Darth's (using ?search)
7. create fixture which will return schema of people object
8. create test which will validate that all people objects contains required schema fields
9. create factory fixture which will return search people results
10. create test which will check that search for any char in English alphabet or any number from 0 to 9 will return number of results >0 except cases of search by 6, 9 and 0. It is not allowed to use loops inside the test body.
11. try to suggest and implement any other meaningful and suitable tests for "get /people" request
12. try to suggest (and implement if possible) any meaningful and suitable tests for "get /people" requests with parameter ?format=wookiee

Feel free to investigate the full api and add more tests for other endpoints which might show your experience and skills in python, pytest and API testing itself

Provide the code and execute command which you use for executing tests. If there are some additional information which we need to know provide it too (for example some another libraries which must be installed)).

Also, execute all tests and provide tests results too (html report is preferable but not mandatory).
