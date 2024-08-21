from django.urls import path
from consumer_good.views import (
    # calss based views
    ConsumerGoodsListView,
    ConsumerGoodsCreateView,
    ConsumerGoodsDetailView,
    HouseholdUsagesUpdateView,
    ConsumerGoodDeleteView,
)


app_name = "consumer_good"
urlpatterns = [
    path(
        "",
        ConsumerGoodsListView.as_view(),
        name="consumer_good_list",
    ),
    path(
        "<int:pk>",
        ConsumerGoodsDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        ConsumerGoodsCreateView.as_view(),
        name="consumer_good_create",
    ),
    path(
        "<int:pk>/update",
        HouseholdUsagesUpdateView.as_view(),
        name="household_consumption_update",
    ),
    path(
        "<int:pk>/delete",
        ConsumerGoodDeleteView.as_view(),
        name="household_consumption_delete",
    ),
]
