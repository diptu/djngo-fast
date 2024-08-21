from django.db import models
from django.urls import reverse
from vehicle_usages.models import VehicleUsages
from household.models import HouseholdUsages
from food.models import FoodConsumption
from consumer_good.models import ConsumerGood
from other.models import OtherUsages


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2", "Tons of Carbon Dioxide"
    # TCO2EQ_PER_KM = "tCO2", "Tons of Carbon Dioxide"


# Create your models here.
class Emission(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_usages = models.ForeignKey(VehicleUsages, on_delete=models.CASCADE)
    household_usages = models.ForeignKey(HouseholdUsages, on_delete=models.CASCADE)
    food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)
    consumer_good = models.ForeignKey(ConsumerGood, on_delete=models.CASCADE)
    other_uages = models.ForeignKey(OtherUsages, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CALCULATED FILDS
    resedential_emission = models.FloatField(default=0)
    resedential_emission = models.FloatField(default=0)
    business_emission = models.FloatField(default=0)
    total_emission = models.FloatField(default=0)

    unit = models.CharField(
        max_length=10,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):
        # print(f"vehicle_footprint:{self.vehicle_usages.vehicle_footprint}")
        self.resedential_emission = (
            self.vehicle_usages.vehicle_footprint
            + self.household_usages.residential_footprint
            + self.food_consumption.food_footprint
            + self.consumer_good.consumer_good_emission
            + self.other_uages.other_emission
        )
        # TODO: UPdate with Business Emissions component
        self.business_emission = 0
        self.total_emission = self.resedential_emission + self.business_emission
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "carbon_footprint:detail", kwargs={"pk": self.pk}
        )  # f"/household/{self.pk}"
