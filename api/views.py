import logging

import aiohttp.web
import ujson as ujson
from aiohttp.web import View
from aiohttp_pydantic import PydanticView

from api.serializers import FreezList
from api.services.reciepts import RecipesProvider

logging.getLogger(__name__)


class GetFoodReсipes(PydanticView):
    """View for get recipes by products."""

    async def post(self, body: FreezList):
        logging.info("Get post request for get recipes with food with data -- {0}".format(body))
        await self.request.app["mongo"].insert_foods(body.products)
        recipes_service = RecipesProvider(body.products)
        recipes_list = recipes_service.count_recipes_with_friz()
        await self.request.app["mongo"].insert_recipes(recipes_list.get("recipes"))
        return aiohttp.web.Response(status=200, text=ujson.dumps(recipes_list), content_type="application/json")


class GetMostPopularProducts(View):
    """View for get user top 10 products."""

    async def get(self):
        logging.info("Get request for get top of popular products")
        food_popular = await self.request.app["mongo"].get_foods_popular()
        logging.info("Found populat food -- {0}".format(food_popular))
        return aiohttp.web.Response(status=200, text=ujson.dumps(food_popular), content_type="application/json")


class GetLastReciepts(View):
    """View for get recipes by user."""
    async def get(self):
        logging.info("Get request for get last found recieps.")
        recipes = await self.request.app["mongo"].get_last_recipes()
        return aiohttp.web.Response(status=200, text=ujson.dumps(recipes), content_type="application/json")