from django.urls import path
from food.views import (
    # calss based views
    FoodConsumptionCreateView,
    FoodConsumptionDetailView,
    FoodConsumptionListView,
    FoodConsumptionUpdateView,
    FoodConsumptionDeleteView,
)


app_name = "food"
urlpatterns = [
    path(
        "",
        FoodConsumptionListView.as_view(),
        name="food_consumption_list",
    ),
    path(
        "<int:pk>",
        FoodConsumptionDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        FoodConsumptionCreateView.as_view(),
        name="food_consumption_create",
    ),
    path(
        "<int:pk>/update",
        FoodConsumptionUpdateView.as_view(),
        name="household_consumption_update",
    ),
    path(
        "<int:pk>/delete",
        FoodConsumptionDeleteView.as_view(),
        name="household_consumption_delete",
    ),
]
