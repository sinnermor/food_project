import logging

import aiohttp.web
from aiohttp.web import Application

import config
from api.routes import inject_routes
from api.services.mongo import MongoClient


async def mongo_client(app: Application) -> None:
    """Function for mongo connect context.

    Yields:
        None
    """
    mongo = MongoClient.create(mongo_url=config.MONGO_URL, mongo_db=config.MONGO_DB)
    await mongo.start()
    app["mongo"] = mongo
    yield
    await app["mongo"].close()


def run():
    logging.basicConfig(level=getattr(logging, config.LOG_LEVEL))
    app = Application()
    inject_routes(app)
    app.cleanup_ctx.extend((mongo_client,))
    aiohttp.web.run_app(app)
