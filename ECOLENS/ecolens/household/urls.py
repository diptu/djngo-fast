from django.urls import path
from household.views import (
    # calss based views
    HouseholdUsagesCreateView,
    HouseholdUsagesDetailView,
    HouseholdUsagesListView,
    HouseholdUsagesUpdateView,
    HouseholdUsagesDeleteView,
)


app_name = "household"
urlpatterns = [
    path(
        "",
        HouseholdUsagesListView.as_view(),
        name="household_usages_list",
    ),
    path(
        "<int:pk>",
        HouseholdUsagesDetailView.as_view(),
        name="detail",
    ),
    path(
        "create",
        HouseholdUsagesCreateView.as_view(),
        name="household_usages_create",
    ),
    path(
        "<int:pk>/update",
        HouseholdUsagesUpdateView.as_view(),
        name="household_usages_update",
    ),
    path(
        "<int:pk>/delete",
        HouseholdUsagesDeleteView.as_view(),
        name="household_usages_delete",
    ),
]
