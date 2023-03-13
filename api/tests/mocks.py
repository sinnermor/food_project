
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
RESPONSE_ONE_RECIPE = {'recipes': [{'name': 'Салат «Русский»', 'count': 1}]}

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