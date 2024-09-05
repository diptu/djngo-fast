from django.urls import path
from .views import (
    # calss based views
    TransportationListView,
    TransportationCreateView,
    TransportationDetailView,
    TransportationUpdateView,
    TransportationDeleteView,
)


app_name = "travel"
urlpatterns = [
    path(
        "",
        TransportationListView.as_view(),
        name="travel_list",
    ),
    path(
        "<int:pk>",
        TransportationDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        TransportationCreateView.as_view(),
        name="travel_create",
    ),
    path(
        "<int:pk>/update",
        TransportationUpdateView.as_view(),
        name="travel_update",
    ),
    path(
        "<int:pk>/delete",
        TransportationDeleteView.as_view(),
        name="vehicle_usages_delete",
    ),
]
