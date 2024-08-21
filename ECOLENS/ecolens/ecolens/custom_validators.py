from django.core.exceptions import ValidationError


def validate_min(value):
    if value < 0:
        raise ValidationError("Cannot be negative.")
