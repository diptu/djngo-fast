from django.core.exceptions import ValidationError
from .custom_choices import DistanceUnit


def validate_min(value):
    if value < 0:
        raise ValidationError("Cannot be negative.")


def validate_distance_unit(value):
    if value not in [choice[0] for choice in DistanceUnit.choices]:
        raise ValidationError("Invalid Unit.")
