import pytest
from magnumopus import create_app
from .. import is_dictionary_inside

async def create_substance_request(client, nature):
    return await client.post('/substance', json={
        'nature': nature
    })

async def index_substances_request(client, nature):
    return await client.get(f'/substance?nature={nature}')

@pytest.mark.asyncio
async def test_create_substance(client):
    rv = await create_substance_request(client, 'Sulphur')

    assert rv.status_code == 201

    content = await rv.get_json()

    assert type(content['id']) is int

    assert is_dictionary_inside({
        'nature': 'Sulphur',
        'state': [],
        'is_philosophers_stone': False
    }, content)


@pytest.mark.asyncio
async def test_get_substances(client):
    await create_substance_request(client, 'Sulphur')

    rv = await index_substances_request(client, 'Sulphur')

    assert rv.status_code == 200

    content = (await rv.get_json())['result']

    assert type(content) is list

    assert len(content) == 1

    assert type(content[0]['id']) is int

    assert is_dictionary_inside({
        'nature': 'Sulphur',
        'state': [],
        'is_philosophers_stone': False
    }, content[0])

# We also need non-happy paths!
