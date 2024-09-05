# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone
from django.urls import reverse
from ecolens.custom_choices import DistanceUnit, CO2EmissionUnit
from ecolens.custom_validators import validate_min, validate_distance_unit
from .utils import (
    BUSINESS_FLIGHT_DISTANCE_CONVERSION_FACTORS,
    BUSINESS_PUBLIC_TRNSIT_CONVERSION_FACTORS,
    BUSINESS_GASOLINE_CAR_MANUFACTURING_EMISSIONS,
    BUSINESS_DIESEL_CAR_MANUFACTURING_EMISSIONS,
    BUSINESS_ELECTRIC_CAR_MANUFACTURING_EMISSIONS,
    BUSINESS_HYBRID_CAR_MANUFACTURING_EMISSIONS,
    BUSINESS_ELECTRIC_CAR_EMISSIONS_PER_KM,
    BUSINESS_HYBRID_CAR_EMISSIONS_PER_KM,
    BUSINESS_GASOLINE_CAR_EMISSIONS_PER_KM,
    BUSINESS_DISEL_CAR_EMISSIONS_PER_KM,
    BUSINESS_ELECTRIC_CAR_EMISSIONS_PER_KM,
    BUSINESS_HYBRID_CAR_EMISSIONS_PER_KM,
    STAFF_GASOLINE_CAR_EMISSIONS_PER_KM,
    STAFF_DISEL_CAR_EMISSIONS_PER_KM,
    STAFF_ELECTRIC_CAR_EMISSIONS_PER_KM,
    STAFF_HYBRID_CAR_EMISSIONS_PER_KM,
)


class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    flight_distance = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="e.g., 1000",
    )
    flight_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    public_transit_distance = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="e.g., 1000",
    )
    transit_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    # No of cars- Company Vehicles
    company_num_of_gasolin_cars = models.IntegerField(default=0, help_text="e.g., 1")
    company_num_of_diesel_cars = models.IntegerField(default=0, help_text="e.g., 1")
    company_num_of_electric_cars = models.IntegerField(default=0, help_text="e.g., 1")
    company_num_of_hybrid_cars = models.IntegerField(default=0, help_text="e.g., 1")

    # Car Milage - Company Vehicles
    company_gasoline_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    company_diesel_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    company_electric_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    company_hybrid_car_driven = models.FloatField(default=0, help_text="e.g., 100")

    # Car Milage - Staff Commute
    staff_gasoline_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    staff_diesel_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    staff_electric_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    staff_hybrid_car_driven = models.FloatField(default=0, help_text="e.g., 100")

    # Car Milage Unit - Company Vehicles
    gasolin_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )
    diesel_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )
    electric_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )
    hybrid_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CALCULATED FILDS
    flight_emission = models.FloatField(default=0)
    public_transit_emission = models.FloatField(default=0)
    # Car Emission - Company Vehicles
    company_gasoline_car_emissions = models.FloatField(default=0)
    company_diesel_car_emissions = models.FloatField(default=0)
    company_electric_car_emissions = models.FloatField(default=0)
    company_hybrid_car_emissions = models.FloatField(default=0)

    # Car Emission - Staff Commute
    staff_gasoline_car_emissions = models.FloatField(default=0)
    staff_diesel_car_emissions = models.FloatField(default=0)
    staff_electric_car_emissions = models.FloatField(default=0)
    staff_hybrid_car_emissions = models.FloatField(default=0)

    vehicle_footprint = models.FloatField(default=0)
    emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):
        self.flight_emission = (
            self.flight_distance
            * BUSINESS_FLIGHT_DISTANCE_CONVERSION_FACTORS[self.flight_unit]
        )
        self.public_transit_emission = (
            self.public_transit_distance
            * BUSINESS_PUBLIC_TRNSIT_CONVERSION_FACTORS[self.transit_unit]
        )

        self.company_gasoline_car_emissions = (
            self.company_gasoline_car_driven
            * BUSINESS_GASOLINE_CAR_EMISSIONS_PER_KM[self.gasolin_car_unit]
        ) + BUSINESS_GASOLINE_CAR_MANUFACTURING_EMISSIONS[self.gasolin_car_unit]

        self.company_diesel_car_emissions = (
            self.company_diesel_car_driven
            * BUSINESS_DISEL_CAR_EMISSIONS_PER_KM[self.diesel_car_unit]
        ) + BUSINESS_DIESEL_CAR_MANUFACTURING_EMISSIONS[self.diesel_car_unit]

        self.company_electric_car_emissions = (
            BUSINESS_ELECTRIC_CAR_EMISSIONS_PER_KM[self.electric_car_unit]
            * self.company_electric_car_driven
        ) + BUSINESS_ELECTRIC_CAR_MANUFACTURING_EMISSIONS[self.electric_car_unit]
        self.company_hybrid_car_emissions = (
            BUSINESS_HYBRID_CAR_EMISSIONS_PER_KM[self.hybrid_car_unit]
            * self.company_hybrid_car_driven
        ) + BUSINESS_HYBRID_CAR_MANUFACTURING_EMISSIONS[self.hybrid_car_unit]

        self.staff_gasoline_car_emissions = (
            self.staff_gasoline_car_driven
            * STAFF_GASOLINE_CAR_EMISSIONS_PER_KM[self.gasolin_car_unit]
        )
        self.staff_diesel_car_emissions = (
            self.staff_diesel_car_driven
            * STAFF_DISEL_CAR_EMISSIONS_PER_KM[self.diesel_car_unit]
        )

        self.staff_electric_car_emissions = (
            self.staff_electric_car_driven
            * STAFF_ELECTRIC_CAR_EMISSIONS_PER_KM[self.electric_car_unit]
        )
        self.staff_hybrid_car_emissions = (
            self.staff_hybrid_car_driven
            * STAFF_HYBRID_CAR_EMISSIONS_PER_KM[self.hybrid_car_unit]
        )
        self.vehicle_footprint = (
            self.flight_emission
            + self.public_transit_emission
            + self.company_gasoline_car_emissions
            + self.company_diesel_car_emissions
            + self.company_electric_car_emissions
            + self.company_hybrid_car_emissions
            + self.staff_gasoline_car_emissions
            + self.staff_diesel_car_emissions
            + self.staff_electric_car_emissions
            + self.staff_hybrid_car_emissions
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "travel:detail", kwargs={"pk": self.pk}
        )  # f"/transportation/{self.pk}"
