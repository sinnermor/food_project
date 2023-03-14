import datetime

import pytest as pytest
from aiohttp.web_app import Application

import config
from api.routes import inject_routes
from api.services.mongo import MongoClient
from api.tests import mocks
from app import mongo_client


@pytest.fixture
def loop(event_loop):
    yield event_loop



@pytest.fixture
def client(loop, aiohttp_client):
    """Фикстура для создания тестового приложения."""
    app = Application()
    inject_routes(app)
    app.cleanup_ctx.extend((mongo_client,))
    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture(autouse=True)
async def setup_db():

    mongo = MongoClient.create(mongo_url=config.MONGO_URL, mongo_db=config.MONGO_DB)
    await mongo.start()

    await mongo.mongo_db[config.RECIPE_INFO_COLLECTION].insert_many(mocks.MONGO_RECIEPTS_DATA
        )
    await mongo.mongo_db[config.PRODUCTS_INFO_COLLECTION].insert_many([
        {"product": "картофель", "user": 1},
        {"product": "картофель", "user": 1},
        {"product": "картофель", "user": 1},
        {"product": "мясо", "user": 1},
        {"product": "мясо", "user": 1},
        {"product": "мясо", "user": 1},
        {"product": "сметана", "user": 1},
        {"product": "яйцо", "user": 1},
        {"product": "огурец", "user": 1},
        {"product": "редис", "user": 1},
        {"product": "помидор", "user": 1},
        {"product": "свекла", "user": 1},
        {"product": "кабачок", "user": 1},
        {"product": "укроп", "user": 1},
        {"product": "лук", "user": 1},
        {"product": "барбарис", "user": 1},
        ]
    )
    yield
    await mongo.mongo_db[config.RECIPE_INFO_COLLECTION].delete_many({})
    await mongo.mongo_db[config.PRODUCTS_INFO_COLLECTION].delete_many({})

