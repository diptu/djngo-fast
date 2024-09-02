from django.urls import path
from vehicle_usages.views import (
    # calss based views
    VehicleUsagesListView,
    VehicleUsagesDetailView,
    VehicleUsagesUpdateView,
    VehicleUsagesCreateView,
    VehicleUsagesDeleteView,
)


app_name = "vehicle_usages"
urlpatterns = [
    path(
        "",
        VehicleUsagesListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>",
        VehicleUsagesDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        VehicleUsagesCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        VehicleUsagesUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        VehicleUsagesDeleteView.as_view(),
        name="delete",
    ),
]
