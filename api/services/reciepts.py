import logging
from typing import Dict, List

from api.utils import get_cook_book


class RecipesProvider:
    """Class for work with food and recipes."""

    def __init__(self, food_list: List):
        self.food_list = {product.name: product.q for product in food_list}
        self.recipes = get_cook_book()

    def count_products(self, recipe_dict: Dict) -> int:
        """Method to count amount of products for recipe.

        Returns:
            count of portions of recipe with food_list
        """
        count = 0
        if not set(recipe_dict.keys()) - set(self.food_list):
            for item, value in self.food_list.items():
                food_count = recipe_dict.get(item)
                if food_count:
                    count = min(count, value // food_count) if count != 0 else food_count
        return count

    def count_recipes_with_friz(self) -> Dict:
        """Method to find all recipes can be cooked with food_list.

        Returns:
            list of recipes and count can be prepared.
        """
        result = []
        for recipe in self.recipes:
            recipe_products = {product.get("item"): product.get("q") for product in recipe.get("components")}
            recipe_count = self.count_products(recipe_products)
            if recipe_count:
                result.append({"name": recipe["name"], "count": recipe_count})
        logging.info("Found recipes for products -- {0}".format(result))
        return {"recipes": result}
