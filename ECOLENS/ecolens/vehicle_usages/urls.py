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
        name="vihicle_usages_list",
    ),
    path(
        "<int:pk>",
        VehicleUsagesDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        VehicleUsagesCreateView.as_view(),
        name="vehicle_usages_create",
    ),
    path(
        "<int:pk>/update",
        VehicleUsagesUpdateView.as_view(),
        name="vehicle_usages_update",
    ),
    path(
        "<int:pk>/delete",
        VehicleUsagesDeleteView.as_view(),
        name="vehicle_usages_delete",
    ),
]
