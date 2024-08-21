from consumer_good.utils import CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2equ", "Tons of Carbon Dioxide Equvalant"
    ECU = "tCO2equ/USD", "equivalent carbon units per dollar"
    # TCO2EQ_PER_KM = "tCO2", "Tons of Carbon Dioxide"


class GoodsAndServices(models.TextChoices):
    C = "CLOTHING"
    A = "APPLIANCES"
    P = "PHARMACEUTICALS"
    F = "FURNITURE"
    H = "HOSPITALITY"
    S = "SERVICES"


def validate_min(value):
    if value < 0.0:
        raise ValidationError("Cannot be negative.")


class ConsumerGood(models.Model):
    id = models.AutoField(primary_key=True)
    clothing = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    appliances = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    pharmaceuticals = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    furniture = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    hospitality = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    services = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,1000",
        blank=False,
    )
    consumption_unit = models.CharField(
        max_length=13,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.ECU,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CALCULATED FILDS
    clothing_emission = models.FloatField(default=0)
    appliances_emission = models.FloatField(default=0)
    pharmaceuticals_emission = models.FloatField(default=0)

    furniture_emission = models.FloatField(default=0)
    hospitality_emission = models.FloatField(default=0)
    services_emission = models.FloatField(default=0)

    consumer_good_emission = models.FloatField(default=0)

    emission_unit = models.CharField(
        max_length=13,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):

        self.clothing_emission = (
            self.clothing
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.C]
            * 12
        )
        self.appliances_emission = (
            self.appliances
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.A]
            * 12
        )
        self.pharmaceuticals_emission = (
            self.pharmaceuticals
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.P]
            * 12
        )

        self.furniture_emission = (
            self.furniture
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.F]
            * 12
        )
        self.hospitality_emission = (
            self.hospitality
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.H]
            * 12
        )
        self.services_emission = (
            self.services
            * CONSUMER_GOODS_AND_SERVICES_CONVERSION_FACTORS[GoodsAndServices.S]
            * 12
        )

        self.consumer_good_emission = (
            self.clothing_emission
            + self.appliances_emission
            + self.pharmaceuticals_emission
            + self.furniture_emission
            + self.hospitality_emission
            + self.services_emission
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "consumer_good:detail", kwargs={"pk": self.pk}
        )  # f"/consumer_good/{self.pk}"
