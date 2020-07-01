import pytest
from magnumopus import create_app
from .. import is_dictionary_inside
from .test_substance_resource import create_substance_request

def create_alembic_instruction_request(client, instruction_type, natures, action=None):
    data = {
        'instruction_type': instruction_type,
        'natures': ','.join(natures)
    }

    if action is not None:
        data['action'] = action

    return client.post('/alembic_instruction', data=data)

def test_create_alembic_mix_instruction(client):
    create_substance_request(client, ['Mercury'])
    create_substance_request(client, ['Salt'])
    create_substance_request(client, ['Sulphur'])

    rv = create_alembic_instruction_request(client, 'mix', ['Mercury', 'Salt', 'Sulphur'])

    assert rv.status_code == 201

    content = rv.get_json()

    assert is_dictionary_inside({
        'nature': 'Gloop',
        'state': [],
        'is_philosophers_stone': False
    }, content)

def test_create_alembic_process_instruction(client):
    create_substance_request(client, ['Mercury'])

    rv = create_alembic_instruction_request(client, 'process', ['Mercury'], 'cook')

    assert rv.status_code == 201

    content = rv.get_json()

    assert is_dictionary_inside({
        'nature': 'Mercury',
        'state': ['cooked'],
        'is_philosophers_stone': False
    }, content)
