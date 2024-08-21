from django.urls import path
from .views import (
    # calss based views
    OtherCreateView,
    OtherListView,
    OtherDetailView,
    OtherUpdateView,
    OtherDeleteView,
)


app_name = "other"
urlpatterns = [
    path(
        "",
        OtherListView.as_view(),
        name="other_list",
    ),
    path(
        "<int:pk>",
        OtherDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        OtherCreateView.as_view(),
        name="other_create",
    ),
    path(
        "<int:pk>/update",
        OtherUpdateView.as_view(),
        name="other_update",
    ),
    path(
        "<int:pk>/delete",
        OtherDeleteView.as_view(),
        name="household_consumption_delete",
    ),
]
