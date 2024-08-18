from django.urls import path
from .views import (
    # calss based views
    EmissionCreateView,
    EmissionListView,
    EmissionDetailView,
    EmissionUpdateView,
    EmissionDeleteView,
)


app_name = "carbon_footprint"
urlpatterns = [
    path(
        "",
        EmissionListView.as_view(),
        name="carbon_footprint_list",
    ),
    path(
        "<int:pk>",
        EmissionDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        EmissionCreateView.as_view(),
        name="carbon_footprint_create",
    ),
    path(
        "<int:pk>/update",
        EmissionUpdateView.as_view(),
        name="arbon_footprint_update",
    ),
    path(
        "<int:pk>/delete",
        EmissionDeleteView.as_view(),
        name="arbon_footprint_delete",
    ),
]
