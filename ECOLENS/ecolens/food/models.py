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
        help_text="""Select the appropriate waste category based on the percentage.
         0%: Minimal Waste, 0 to 10%: Low Waste, 10 to 25%:Moderate Waste, >255%: High Waste""",
    )
    level_of_wastage = models.CharField(
        max_length=10,
        choices=WasteLabel.choices,
        default=WasteLabel.LW,
        blank=False,
        help_text="""Select the appropriate waste category based on the percentage.
         0%: Minimal Waste, 0 to 10%: Low Waste, 10 to 25%:Moderate Waste, >255%: High Waste""",
    )

    consumption_unit = models.CharField(
        max_length=12,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2_Y,
        blank=False,
    )

    # Vehicle_usages = models.ForeignKey(VehicleUsages, on_delete=models.CASCADE)
    # household_usages = models.ForeignKey(
    #     HouseholdUsages,
    #     on_delete=models.CASCADE,
    # )

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
        )
        self.wastage_emission = (
            0.564290 * WASTE_LABEL_CONVERSION_FACTORS[self.level_of_wastage]
        )
        self.food_footprint = self.diet_emission + self.wastage_emission
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})  # f"/household/{self.pk}"
