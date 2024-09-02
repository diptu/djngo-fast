class General(models.Model):
    id = models.AutoField(primary_key=True)
    num_people = models.IntegerField(
        default=1,
        help_text="Amount in USD,e.g.,2",
        blank=False,
    )


class OtherUsages(models.Model):
    id = models.AutoField(primary_key=True)
    education = models.FloatField(
        default=0,
        help_text="Amount in USD,e.g.,500",
        blank=False,
    )
    general = models.ForeignKey(General, on_delete=models.CASCADE)
    public_services_emission = models.FloatField(default=0)

    def save(self, *args, **kwargs):

        self.public_services_emission = 12 * self.general.num_people
        super().save(*args, **kwargs)
