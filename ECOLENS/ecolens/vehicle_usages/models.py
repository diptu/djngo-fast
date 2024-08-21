# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone
from django.urls import reverse
from .utils import (
    DistanceUnit,
    FLIGHT_DISTANCE_CONVERSION_FACTORS,
    PUBLIC_TRNSIT_CONVERSION_FACTORS,
    GASOLINE_CAR_MANUFACTURING_EMISSIONS,
    DIESEL_CAR_MANUFACTURING_EMISSIONS,
    ELECTRIC_CAR_MANUFACTURING_EMISSIONS,
    HYBRID_CAR_MANUFACTURING_EMISSIONS,
    GASOLINE_CAR_EMISSIONS_PER_KM,
    DISEL_CAR_EMISSIONS_PER_KM,
    ELECTRIC_CAR_EMISSIONS_PER_KM,
    HYBRID_CAR_EMISSIONS_PER_KM,
)

from django.core.exceptions import ValidationError


def validate_min_distance(value):
    if value < 0.0:
        raise ValidationError("Distance cannot be negative.")


def validate_distance_unit(value):
    if value not in [choice[0] for choice in DistanceUnit.choices]:
        raise ValidationError("Invalid Unit. Choose from Kilometer or Mile.")


class DistanceUnit(models.TextChoices):
    Km = "Km", "Kilometer"
    Mi = "Mi", "Mile"


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2equ", "Tons of Carbon Dioxide Equvalant"
    TCO2_Y = "tCO2equ/year", "Tons of Carbon Dioxide Equvalant per year"


class VehicleUsages(models.Model):
    id = models.AutoField(primary_key=True)
    flight_distance = models.FloatField(
        default=0,
        validators=[validate_min_distance],
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
        validators=[validate_min_distance],
        help_text="e.g., 1000",
    )
    transit_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    # No of cars
    num_of_gasolin_cars = models.IntegerField(default=0, help_text="e.g., 1")
    num_of_diesel_cars = models.IntegerField(default=0, help_text="e.g., 1")
    num_of_electric_cars = models.IntegerField(default=0, help_text="e.g., 1")
    num_of_hybrid_cars = models.IntegerField(default=0, help_text="e.g., 1")
    # Car Milage & Unit
    gasoline_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    gasolin_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )
    diesel_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    diesel_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    electric_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    electric_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    hybrid_car_driven = models.FloatField(default=0, help_text="e.g., 100")
    hybrid_car_unit = models.CharField(
        max_length=2,
        choices=DistanceUnit.choices,
        default=DistanceUnit.Km,
        blank=False,
        validators=[validate_distance_unit],
    )

    # CALCULATED FILDS
    flight_emission = models.FloatField(default=0)
    flight_emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    public_transit_emission = models.FloatField(default=0)
    transit_emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    gasoline_car_emissions = models.FloatField(default=0)
    gasoline_car_emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    diesel_car_emissions = models.FloatField(default=0)
    diesel_car_emissions_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    electric_car_emissions = models.FloatField(default=0)
    electric_car_emissions_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    hybrid_car_emissions = models.FloatField(default=0)
    hybrid_car_emissions_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    vehicle_footprint = models.FloatField(default=0)
    vehicle_footprint_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.flight_emission = (
            self.flight_distance * FLIGHT_DISTANCE_CONVERSION_FACTORS[self.flight_unit]
        )

        self.public_transit_emission = (
            self.public_transit_distance
            * PUBLIC_TRNSIT_CONVERSION_FACTORS[self.transit_unit]
        )
        print(f"public_transit_emission: {self.public_transit_emission},")
        self.gasoline_car_emissions = (
            self.gasoline_car_driven
            * GASOLINE_CAR_EMISSIONS_PER_KM[self.gasolin_car_unit]
        ) + GASOLINE_CAR_MANUFACTURING_EMISSIONS[self.gasolin_car_unit]

        self.diesel_car_emissions = (
            self.diesel_car_driven * DISEL_CAR_EMISSIONS_PER_KM[self.diesel_car_unit]
        ) + DIESEL_CAR_MANUFACTURING_EMISSIONS[self.diesel_car_unit]

        self.electric_car_emissions = (
            ELECTRIC_CAR_EMISSIONS_PER_KM[self.electric_car_unit]
            * self.electric_car_driven
        ) + ELECTRIC_CAR_MANUFACTURING_EMISSIONS[self.electric_car_unit]
        self.hybrid_car_emissions = (
            HYBRID_CAR_EMISSIONS_PER_KM[self.hybrid_car_unit] * self.hybrid_car_driven
        ) + HYBRID_CAR_MANUFACTURING_EMISSIONS[self.hybrid_car_unit]

        self.vehicle_footprint = (
            self.flight_emission
            + self.public_transit_emission
            + self.gasoline_car_emissions
            + self.diesel_car_emissions
            + self.electric_car_emissions
            + self.hybrid_car_emissions
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "vehicle_usages:detail", kwargs={"pk": self.pk}
        )  # f"/vehicle_usages/{self.pk}"
