import ujson

from api.tests import mocks


async def test_get_one_recept(client):
    response = await client.request(
        method="POST",
        path="/api/v1/recipes",
        data=ujson.dumps(mocks.REQUEST_ONE_RECIPE)
    )

    response_json = await response.json()
    assert response.status == 200
    assert response_json == mocks.RESPONSE_ONE_RECIPE


async def test_get_recept_none(client):
    response = await client.request(
        method="POST",
        path="/api/v1/recipes",
        data=ujson.dumps(mocks.REQUEST_NO_RECIPE)
    )

    response_json = await response.json()
    assert response.status == 200
    assert response_json == {"recipes": []}


async def test_get_recipes_many(client):
    """Тест на получение всех записей из MongoDB."""
    response = await client.request(
        method="POST",
        path="/api/v1/recipes",
        data=ujson.dumps(mocks.REQUEST_MULTY_RECIPES)
    )
    response_json = await response.json()
    assert response.status == 200
    assert response_json == mocks.RESPONSE_MULTY_RECIPES

