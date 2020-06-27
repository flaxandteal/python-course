import pytest
from magnumopus import create_app
from .. import is_dictionary_inside

def create_substance_request(client, nature):
    return client.post('/substance', data={
        'nature': nature
    })

def index_substances_request(client, nature):
    return client.get(f'/substance?nature={nature}')

def test_create_substance(client):
    rv = create_substance_request(client, 'Sulphur')

    assert rv.status_code == 201

    content = rv.get_json()

    assert type(content['id']) is int

    assert is_dictionary_inside({
        'nature': 'Sulphur',
        'state': [],
        'is_philosophers_stone': False
    }, content)


def test_get_substances(client):
    create_substance_request(client, 'Sulphur')

    rv = index_substances_request(client, 'Sulphur')

    assert rv.status_code == 200

    content = rv.get_json()

    assert type(content) is list

    assert len(content) == 1

    assert type(content[0]['id']) is int

    assert is_dictionary_inside({
        'nature': 'Sulphur',
        'state': [],
        'is_philosophers_stone': False
    }, content[0])

# We also need non-happy paths!
