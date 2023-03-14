import datetime

REQUEST_NO_RECIPE = {"products": [
        {"name": "мясо",
         "q": 300
         },
    ]
    }

REQUEST_ONE_RECIPE = {"products": [
        {"name": "мясо",
         "q": 300
         },
        {
            "name": "картофель",
            "q":4
        },
    ]
    }
RESPONSE_ONE_RECIPE = {'recipes': [{'name': 'Салат «Ленинградский»', 'count': 1}]}

REQUEST_MULTY_RECIPES = {"products": [
        {"name": "мясо",
         "q": 1000
         },
        {
            "name": "картофель",
            "q":9
        },
        {
                    "name": "огурец",
                    "q": 2
                }
    ]
    }

RESPONSE_MULTY_RECIPES = {'recipes': [{'name': 'Салат «Русский»', 'count': 1}, {'name': 'Салат «Ленинградский»', 'count': 3}]}
date_mongo = datetime.datetime.now() - datetime.timedelta(minutes=2)

MONGO_RECIEPTS_DATA = [
        {"date": date_mongo, "recipe": "Салат «Ленинградский»", "user": 1},
        {"date": date_mongo, "recipe": "Салат «Русский»", "user": 1},
        {"date": date_mongo, "recipe": "Салат с рыбой и овощами", "user": 1},
        {"date": date_mongo, "recipe": "Салат «Ленинградский»", "user": 1},
    ]

RECIPES_RESPONSE ={'user': 1, 'last_recieps': [['Салат «Ленинградский»', 'Салат «Русский»', 'Салат с рыбой и овощами', 'Салат «Ленинградский»']]}

POPULAR_PRODUCTS_RESPONSE = [{'_id': 'мясо', 'count_new': 3}, {'_id': 'картофель', 'count_new': 3}, {'_id': 'свекла', 'count_new': 1}, {'_id': 'яйцо', 'count_new': 1}, {'_id': 'кабачок', 'count_new': 1}, {'_id': 'помидор', 'count_new': 1}, {'_id': 'огурец', 'count_new': 1}, {'_id': 'лук', 'count_new': 1}, {'_id': 'барбарис', 'count_new': 1}, {'_id': 'сметана', 'count_new': 1}]