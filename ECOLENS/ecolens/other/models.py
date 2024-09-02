from django.db import models
from django.urls import reverse

from other.utils import OTHERS_CONVERSION_FACTORS
from general.models import General

from ecolens.custom_validators import validate_min
from ecolens.custom_choices import (
    CO2EmissionUnit,
    Miscellaneous,
)

from django.db.models.signals import post_save
from django.dispatch import receiver


class OtherUsages(models.Model):
    id = models.AutoField(primary_key=True)
    education = models.FloatField(
        default=0,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,500",
        blank=False,
    )
    activities = models.FloatField(
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

    general = models.ForeignKey(General, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CALCULATED FILDS
    education_emission = models.FloatField(default=0)
    activities_emission = models.FloatField(default=0)
    public_services_emission = models.FloatField(default=0)

    other_emission = models.FloatField(default=0)

    emission_unit = models.CharField(
        max_length=13,
        choices=CO2EmissionUnit.choices,
        default=CO2EmissionUnit.TCO2,
        blank=False,
    )

    def save(self, *args, **kwargs):

        self.education_emission = (
            self.education * OTHERS_CONVERSION_FACTORS[Miscellaneous.E] * 12
        )
        self.activities_emission = (
            self.activities * OTHERS_CONVERSION_FACTORS[Miscellaneous.A] * 12
        )
        self.public_services_emission = (
            OTHERS_CONVERSION_FACTORS[Miscellaneous.P] * self.general.num_people
        )

        self.other_emission = (
            self.education_emission
            + self.activities_emission
            + self.public_services_emission
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "other:detail", kwargs={"pk": self.pk}
        )  # f"/miscellaneous/{self.pk}"


@receiver(post_save, sender=General)
def update_other_usages(sender, instance, **kwargs):
    if not kwargs.get("created", False):  # Only update on updates
        OtherUsages.objects.filter(general=instance).update(
            public_services_emission=OTHERS_CONVERSION_FACTORS[Miscellaneous.P]
            * instance.num_people
        )
