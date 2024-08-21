from django.db import models
from django.urls import reverse
from ecolens.custom_validators import validate_min


class General(models.Model):
    id = models.AutoField(primary_key=True)
    num_people = models.IntegerField(
        default=1,
        validators=[validate_min],
        help_text="Amount in USD,e.g.,2",
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(
            "general:detail", kwargs={"pk": self.pk}
        )  # f"/miscellaneous/{self.pk}"
