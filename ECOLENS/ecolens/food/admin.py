from django.contrib import admin

# Register your models here.
from .models import FoodConsumption

admin.site.register(
    FoodConsumption,
)
