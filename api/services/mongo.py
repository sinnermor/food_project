import datetime
import logging
from typing import Dict, List

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.errors import PyMongoError

import config


class MongoClient:
    """Базовый класс для работы с транзакциями."""

    def __init__(self, motor_client: AsyncIOMotorClient, mongo_db: AsyncIOMotorDatabase):
        self.motor_client = motor_client
        self.mongo_db = mongo_db

    @classmethod
    def create(cls, mongo_url: str, mongo_db: str):  # type: ignore
        """Метод для создания и запуска клиента Redis.

        Args:
            mongo_url: урл подключения к Моного.
            mongo_db: имя бд Монго.

        Returns:
            экземпляр класса
        """
        motor_client = AsyncIOMotorClient(mongo_url)
        mongo_db = motor_client[mongo_db]
        return cls(motor_client=motor_client, mongo_db=mongo_db)

    async def close(self) -> None:
        """Метод для закрытия соединения с Монго."""
        self.motor_client.close()
        logging.info("The MongoDB connection is closed!")

    async def start(self) -> None:
        """Метод для проверки соединения с Монго.

        Raises:
            PyMongoError: ошибка в Монго
        """
        try:
            await self.mongo_db.command("ping")
        except PyMongoError as exc:
            logging.error("Error connect to MongoDB: {0}".format(str(exc)))
            raise

    async def insert_foods(self, food_list: List):
        """Method to insert called food products to Mongo."""

        for food in food_list:
            logging.info("Start insert to Mongo value {0}".format(food.name))
            await self.mongo_db["food_popular"].insert_one({"user":1, "product": food.name})
        logging.info("Food list was successfully added to Mongp.")

    async def insert_recipes(self, recipe_list: List) -> None:
        """Method to insert counted recipes to Mongo."""
        for recipe in recipe_list:
            recipre_name = recipe.get("name")
            logging.info("Start insert to Mongo value {0}".format(recipre_name))
            await self.mongo_db["recipes"].insert_one({
                "user": 1, "recipe": recipre_name, "date": datetime.datetime.now()
            })
            logging.info("Recipes was successfully added to Mongp.")

    async def get_foods_popular(self) -> List:
        """Method to get list of most popular products from friz."""
        logging.info("Started get top 10 popular food")
        popular_food_cursor = self.mongo_db["food_popular"].aggregate([
            {
                "$group":
                    {
                        "_id": "$product",
                        "count_new": {"$sum": 1}
                    },
            },
            {"$sort": {'count_new': -1}},
            {"$limit": 10}
        ]
        )
        return await popular_food_cursor.to_list(length=10)

    async def get_last_recipes(self) -> Dict:
        """Method to get recipes list of last hour."""
        last_recipes = []
        time_param = datetime.datetime.now() - datetime.timedelta(minutes=config.RECIPES_TIME_DELTA)
        last_recieps = self.mongo_db["recipes"].find({"date": {"$gte": time_param}})
        async for document in last_recieps:
            last_recipes.append(document.get("recipe"))
        logging.info("Found {} last recipes.".format(len(last_recipes)))
        return {"user": 1, "last_recieps": [last_recipes]}
