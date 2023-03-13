from aiohttp.web import Application, view

from api import views


def inject_routes(app: Application):

    app.add_routes([
        view("/api/v1/recipes", views.GetFoodReсipes),
        view("/api/v1/info/recipes", views.GetLastReciepts),
        view("/api/v1/info/popular", views.GetMostPopularProducts),
    ])