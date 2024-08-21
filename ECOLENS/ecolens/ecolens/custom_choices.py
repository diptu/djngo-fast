from django.db import models


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2equ", "Tons of Carbon Dioxide Equvalant"
    ECU = "tCO2equ/USD", "equivalent carbon units per dollar"
    # TCO2EQ_PER_KM = "tCO2", "Tons of Carbon Dioxide"


class Miscellaneous(models.TextChoices):
    E = "EDUCATION"
    A = "ACTIVITIES"
    P = "PUBLIC_SERVICES"
