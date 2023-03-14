import ujson

from api.tests import mocks



async def test_get_last_reciepts(client):
    response = await client.request(
        method="GET",
        path="api/v1/info/recipes",
    )

    response_json = await response.json()
    assert response.status == 200
    assert response_json == mocks.RECIPES_RESPONSE

async def test_get_popular_products(client):
    response = await client.request(
        method="GET",
        path="/api/v1/info/popular",
    )

    response_json = await response.json()
    assert response.status == 200
    assert len(response_json) == 10
    assert response_json == mocks.POPULAR_PRODUCTS_RESPONSE
