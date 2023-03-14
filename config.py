import os

env = os.environ.get


LOG_LEVEL = env("LOG_LEVEL", "INFO")
MONGO_USER = env("MONGO_USER", "mongoadmin")
MONGO_PASSWORD = env("MONGO_PASSWORD", "mongoadmin")
MONGO_HOST = env("MONGO_HOST", "localhost")
MONGO_DB = env("MONGO_DB", "recipes")
MONGO_URL = "mongodb://{0}:{1}@{2}".format(MONGO_USER, MONGO_PASSWORD, MONGO_HOST)
RECIPE_INFO_COLLECTION = env("RECIPE_INFO_COLLECTION", "recipes")
PRODUCTS_INFO_COLLECTION = env("PRODUCTS_INFO_COLLECTION", "food_popular")

RECIPES_TIME_DELTA = env("RECIPES_TIME_DELTA", 60)
FILE_PATH = env("FILE_PATH", "/Users/anastasiy.kordyukova/PycharmProjects/food_project/task.json")