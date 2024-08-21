from django.db import models
from django.urls import reverse
from food.choices import (
    CO2EmissionUnit,
    DietType,
    ConsumptionLabel,
    WasteLabel,
)
from food.utils import (
    FOOD_TYPE_CONVERSION_FACTORS,
    FOOD_CONSUMPTION_CONVERSION_FACTORS,
    WASTE_LABEL_CONVERSION_FACTORS,
)
from django.core.exceptions import ValidationError

from general.models import General


def validate_wastage_label(value):
    if value < 0.0 or value > 1.0:
        raise ValidationError("Invalid input. Input must be between 0 and 1.")


class FoodConsumption(models.Model):
    id = models.AutoField(primary_key=True)
    diet_type = models.CharField(
        max_length=2,
        choices=DietType.choices,
        default=DietType.VI,
        blank=False,
    )

    consumption_level = models.CharField(
        max_length=8,
        choices=ConsumptionLabel.choices,
        default=ConsumptionLabel.LWC,
        blank=False,
        help_text="""Select the appropriate waste category based on the percentage.""",
    )

    level_of_wastage = models.FloatField(
        default=0.0,
        validators=[validate_wastage_label],
        help_text="e.g. 0.3 to represent 30%",
        blank=False,
    )
    consumption_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2_Y,
        blank=False,
    )

    general = models.ForeignKey(General, on_delete=models.CASCADE)

    # CALCULATED FILDS
    diet_emission = models.FloatField(default=0)
    diet_emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )
    wastage_emission = models.FloatField(default=0)
    wastage_emission_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    food_footprint = models.FloatField(default=0)
    food_footprint_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):

        self.diet_emission = (
            FOOD_TYPE_CONVERSION_FACTORS[self.diet_type]
            * FOOD_CONSUMPTION_CONVERSION_FACTORS[self.consumption_level]
            * self.general.num_people
        )
        self.wastage_emission = (
            0.564290
            * FOOD_CONSUMPTION_CONVERSION_FACTORS[self.consumption_level]
            * self.level_of_wastage
            * self.general.num_people
        )
        self.food_footprint = self.diet_emission + self.wastage_emission
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})  # f"/household/{self.pk}"
