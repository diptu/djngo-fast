from django.db import models


class CO2EmissionUnit(models.TextChoices):
    TCO2 = "tCO2equ", "Tons of Carbon Dioxide Equvalant"
    TCO2_Y = "tCO2equ/year", "Tons of Carbon Dioxide Equvalant per year"


class DietType(models.TextChoices):
    VI = ("VI", "Vegan")
    VG = ("VG", "Vegetarian")
    FL = ("FL", "Flexitarian")
    PE = ("PE", "PESCETARIAN")
    OM = ("OM", "Omnivore")
    CA = ("CA", "CARNIVORE")
    KE = ("KE", "KETO")
    PA = ("PA", "PALEO")


class ConsumptionLabel(models.TextChoices):
    MIC = ("Minimal", "Minimal consumption")
    LWC = ("Low", "Low consumption")
    MDC = ("Moderate", "Moderate consumption")
    HGC = ("High", "High Consumption")


class WasteLabel(models.TextChoices):
    MW = ("0%", "Minimal")
    LW = ("0 to 10%", "Low")
    MD = ("10 to 25%", "Moderate")
    HG = ("> 25%", "High")
