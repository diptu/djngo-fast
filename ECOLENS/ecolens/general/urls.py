from django.urls import path
from .views import (
    # calss based views
    GeneralCreateView,
    GeneralListView,
    GeneralUpdateView,
    GeneralDetailView,
    GeneralDeleteView,
)


app_name = "general"
urlpatterns = [
    path(
        "list/",
        GeneralListView.as_view(),
        name="general_list",
    ),
    path(
        "<int:pk>",
        GeneralDetailView.as_view(),
        name="detail",
    ),
    path(
        "",
        GeneralCreateView.as_view(),
        name="general_create",
    ),
    path(
        "<int:pk>/update",
        GeneralUpdateView.as_view(),
        name="general_update",
    ),
    path(
        "<int:pk>/delete",
        GeneralDeleteView.as_view(),
        name="general_delete",
    ),
]
