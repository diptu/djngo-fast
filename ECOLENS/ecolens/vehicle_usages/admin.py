from django.contrib import admin

# Register your models here.
from .models import VehicleUsages


class VehicleUsagesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "flight_distance",
        "public_transit_distance",
        "num_of_gasolin_cars",
        "num_of_diesel_cars",
        "num_of_electric_cars",
        "num_of_hybrid_cars",
        "gasoline_car_driven",
        "diesel_car_driven",
        "electric_car_driven",
        "hybrid_car_driven",
        "created_at",
        "updated_at",
    ]
    search_fields = ["id", "flight_distance"]


admin.site.register(VehicleUsages, VehicleUsagesAdmin)
