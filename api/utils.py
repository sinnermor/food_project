import functools

import ujson

import config


@functools.lru_cache(maxsize=16)
def get_cook_book():
    """Method for get cook book and write to cache."""
    with open(config.FILE_PATH, "r") as f:
        recipe_dict = ujson.load(f)
    return recipe_dict.get("recipes")
