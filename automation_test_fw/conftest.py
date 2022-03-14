# Define global variables here in this file
import pytest


@pytest.fixture
def api():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture
def post():
    return {"userId": 1, "title": "Create a new post with postID 1",  "body": "Discussion contents are posted here"}


@pytest.fixture
def header():
    return {'Content-type': 'application/json; charset=UTF-8'}


@pytest.fixture
def login_post():
    return {
        "username": "mor_2314",
        "password": "83r5^_"
    }

