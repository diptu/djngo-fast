# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone
from django.urls import reverse

from .utils import (
    ELECTRICITY_EMISSION_CONVERSION_FACTORS,
    RENUAL_ENERGY_EMISSION_CONVERSION_FACTORS,
    NATURAL_GAS_EMISSIONS_CONVERSION_FACTORS,
    HEATING_OIL_USAGES_EMISSIONS_CONVERSION_FACTORS,
    WATER_USAGES_EMISSIONS_CONVERSION_FACTORS,
    LIVING_SPACE_CONSTRUCTION_EMISSION_CONVERSION_FACTORS,
    WASTE_RECYCLING_EMISSIONS_CONVERSION_FACTORS,
    WASTE_INCINERATION_EMISSIONS_CONVERSION_FACTORS,
)

from django.core.exceptions import ValidationError


class EnergyUnit(models.TextChoices):
    KWh = "KWh", "Kilowatt-hour"
    # Wh = "Wh", "Watt-hour"


class VolumeUnit(models.TextChoices):
    L = "L", "Liter"
    # KL = "KL", "Kiloliter"


class AreaUnit(models.TextChoices):
    m2 = "m2", "Square meter"


class MassUnit(models.TextChoices):
    Kg = "Kg", "Kilo-gram"
    # lb = "lb", "Pound"


def validate_min_energy(value):
    if value < 0.0:
        raise ValidationError("Energy usages cannot be negative.")


def validate_min_volume(value):
    if value < 0.0:
        raise ValidationError("Usages cannot be negative.")


def validate_min_area(value):
    if value < 0:
        raise ValidationError("Area usages cannot be negative.")


def validate_min_mass(value):
    if value < 0:
        raise ValidationError("Mas usages cannot be negative.")


def validate_energy_unit(value):
    if value not in [choice[0] for choice in EnergyUnit.choices]:
        raise ValidationError("Invalid Unit. Choose from Kilowatt-hour or Watt-hour.")


def validate_share_of_renewable_energy(value):
    if value < 0.0 or value > 1.0:
        raise ValidationError(
            "Invalid input. Reneual energy share must be between 0 and 100%."
        )


def validate_volume_unit(value):
    if value not in [choice[0] for choice in VolumeUnit.choices]:
        raise ValidationError("Invalid Unit. Choose from Liter or Kiloliter.")


def validate_area_unit(value):
    if value not in [choice[0] for choice in AreaUnit.choices]:
        raise ValidationError("Invalid Unit. Choose from m2 or km2.")


def validate_mass_unit(value):
    if value not in [choice[0] for choice in MassUnit.choices]:
        raise ValidationError("Invalid Unit. Choose from kg or lb.")


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2equ", "Tons of Carbon Dioxide Equvalant"
    # TCO2EQ_PER_KM = "tCO2", "Tons of Carbon Dioxide"


class HouseholdUsages(models.Model):
    id = models.AutoField(primary_key=True)
    electricity_consumption = models.FloatField(
        default=0, validators=[validate_min_energy], help_text="e.g., 1000", blank=False
    )
    share_of_renewable_energy = models.FloatField(
        default=0.0,
        validators=[validate_share_of_renewable_energy],
        help_text="e.g. 0.3 to represent 30%",
        blank=False,
    )
    electricity_consumption_unit = models.CharField(
        max_length=3,
        choices=EnergyUnit.choices,
        default=EnergyUnit.KWh,
        blank=False,
        validators=[validate_energy_unit],
    )
    natural_gas_consumption = models.FloatField(
        default=0, validators=[validate_min_energy], help_text="e.g., 1000", blank=False
    )
    natural_gas_consumption_unit = models.CharField(
        max_length=3,
        choices=EnergyUnit.choices,
        default=EnergyUnit.KWh,
        blank=False,
        validators=[validate_energy_unit],
    )
    heating_oil_consumption = models.FloatField(
        default=0,
        validators=[validate_min_volume],
        help_text="e.g., 1000",
        blank=False,
    )
    heating_oil_consumption_unit = models.CharField(
        max_length=2,
        choices=VolumeUnit.choices,
        default=VolumeUnit.L,
        blank=False,
        validators=[validate_volume_unit],
    )
    water_consumption = models.FloatField(
        default=0,
        validators=[validate_min_volume],
        help_text="e.g., 1000",
        blank=False,
    )
    water_consumption_unit = models.CharField(
        max_length=2,
        choices=VolumeUnit.choices,
        default=VolumeUnit.L,
        blank=False,
        validators=[validate_volume_unit],
    )
    living_space = models.IntegerField(
        default=0,
        validators=[validate_min_area],
        help_text="e.g., 1000",
        blank=False,
    )
    living_space_unit = models.CharField(
        max_length=2,
        choices=AreaUnit.choices,
        default=AreaUnit.m2,
        blank=False,
        validators=[validate_area_unit],
    )
    waste_recycling = models.FloatField(
        default=0,
        validators=[validate_min_mass],
        help_text="e.g., 1000",
        blank=False,
    )

    waste_recycling_unit = models.CharField(
        max_length=2,
        choices=MassUnit.choices,
        default=MassUnit.Kg,
        blank=False,
        validators=[validate_mass_unit],
    )
    waste_incineration = models.FloatField(
        default=0,
        validators=[validate_min_mass],
        help_text="e.g., 1000",
        blank=False,
    )
    waste_incineration_unit = models.CharField(
        max_length=2,
        choices=MassUnit.choices,
        default=MassUnit.Kg,
        blank=False,
        validators=[validate_mass_unit],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CALCULATED FILDS
    electricity_consumption_emission = models.FloatField(default=0)
    electricity_consumption_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    renewable_energy = models.FloatField(default=0)
    natural_gas_consumption_emission = models.FloatField(default=0)
    natural_gas_consumption_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    heating_oil_consumption_emission = models.FloatField(default=0)
    heating_oil_consumption_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    water_consumption_emission = models.FloatField(default=0)
    water_consumption_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    living_space_emission = models.FloatField(default=0)
    living_space_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    waste_recycling_emission = models.FloatField(default=0)
    waste_recycling_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    waste_incineration_emission = models.FloatField(default=0)
    waste_incineration_emission_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    residential_footprint = models.FloatField(default=0)
    residential_footprint_unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):
        self.electricity_consumption_emission = (
            self.electricity_consumption
            * (1 - self.share_of_renewable_energy)
            * ELECTRICITY_EMISSION_CONVERSION_FACTORS[self.electricity_consumption_unit]
        ) + (
            self.electricity_consumption
            * self.share_of_renewable_energy
            * RENUAL_ENERGY_EMISSION_CONVERSION_FACTORS[
                self.electricity_consumption_unit
            ]
        )
        self.renewable_energy = (
            self.electricity_consumption * self.share_of_renewable_energy
        )
        self.natural_gas_consumption_emission = (
            self.natural_gas_consumption
            * NATURAL_GAS_EMISSIONS_CONVERSION_FACTORS[
                self.natural_gas_consumption_unit
            ]
        )
        self.heating_oil_consumption_emission = (
            self.heating_oil_consumption
            * HEATING_OIL_USAGES_EMISSIONS_CONVERSION_FACTORS[
                self.heating_oil_consumption_unit
            ]
        )
        self.water_consumption_emission = (
            self.water_consumption
            * WATER_USAGES_EMISSIONS_CONVERSION_FACTORS[self.water_consumption_unit]
        )
        self.living_space_emission = (
            self.living_space
            * LIVING_SPACE_CONSTRUCTION_EMISSION_CONVERSION_FACTORS[
                self.living_space_unit
            ]
        )
        self.waste_recycling_emission = (
            self.waste_recycling
            * WASTE_RECYCLING_EMISSIONS_CONVERSION_FACTORS[self.waste_recycling_unit]
        )

        self.waste_incineration_emission = (
            self.waste_incineration
            * WASTE_INCINERATION_EMISSIONS_CONVERSION_FACTORS[
                self.waste_incineration_unit
            ]
        )

        self.residential_footprint = (
            self.electricity_consumption_emission
            + self.natural_gas_consumption_emission
            + self.heating_oil_consumption_emission
            + self.water_consumption_emission
            + self.living_space_emission
            + self.waste_recycling_emission
            + self.waste_incineration_emission
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "household:detail", kwargs={"pk": self.pk}
        )  # f"/household/{self.pk}"
