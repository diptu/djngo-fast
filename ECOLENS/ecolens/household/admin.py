from django.contrib import admin

# Register your models here.
from .models import HouseholdUsages

admin.site.register(
    HouseholdUsages,
)
