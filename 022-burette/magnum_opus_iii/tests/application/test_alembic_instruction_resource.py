import pytest
from magnumopus import create_app
from .. import is_dictionary_inside
from .test_substance_resource import create_substance_request

async def create_alembic_instruction_request(client, instruction_type, natures, action=None):
    data = {
        'instruction_type': instruction_type,
        'natures': ','.join(natures)
    }

    if action is not None:
        data['action'] = action

    return await client.post('/alembic_instruction', json=data)

@pytest.mark.asyncio
async def test_create_alembic_mix_instruction(client):
    await create_substance_request(client, 'Mercury')
    await create_substance_request(client, 'Salt')
    await create_substance_request(client, 'Sulphur')

    rv = await create_alembic_instruction_request(client, 'mix', ['Mercury', 'Salt', 'Sulphur'])

    assert rv.status_code == 201

    content = await rv.get_json()

    assert is_dictionary_inside({
        'nature': 'Gloop',
        'state': [],
        'is_philosophers_stone': False
    }, content)

@pytest.mark.asyncio
async def test_create_alembic_process_instruction(client):
    await create_substance_request(client, 'Mercury')

    rv = await create_alembic_instruction_request(client, 'process', ['Mercury'], 'cook')

    assert rv.status_code == 201

    content = await rv.get_json()

    assert is_dictionary_inside({
        'nature': 'Mercury',
        'state': ['cooked'],
        'is_philosophers_stone': False
    }, content)
