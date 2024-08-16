from django import forms
from .models import VehicleUsages

DISTANCE_CHOICES = (
    ("Km", "Kilometer"),
    ("Mi", "Mile"),
)


class VehicleUsagesForm(forms.ModelForm):

    flight_distance = forms.DecimalField(min_value=0, decimal_places=2, initial=0)
    flight_unit = forms.ChoiceField(
        choices=DISTANCE_CHOICES,
        required=True,
        initial=DISTANCE_CHOICES[0],
        error_messages={
            "required": "Please select a Unit.",
            "invalid_choice": "Invalid Unit choice.",
        },
    )
    public_transit_distance = forms.DecimalField(
        min_value=0, decimal_places=2, initial=0
    )
    transit_unit = forms.ChoiceField(
        choices=DISTANCE_CHOICES,
        required=True,
        initial=DISTANCE_CHOICES[0],
        error_messages={
            "required": "Please select a Unit.",
            "invalid_choice": "Invalid Unit choice.",
        },
    )

    class Meta:
        model = VehicleUsages
        # Limit the input fields
        fields = [
            "flight_distance",
            "flight_unit",
            "public_transit_distance",
            "transit_unit",
        ]

    def clean(self):
        value = self.cleaned_data
        return value
