import pytest as pytest
from aiohttp.web_app import Application

from api.routes import inject_routes
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

