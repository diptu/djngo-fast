from django import forms
from .models import HousehodUsages

ENEERGY_UNIT_CHOICES = (
    ("KWh", "Kilowatt-hour"),
    ("Wh", "Watt-hour"),
)


class HouseholdeUsagesForm(forms.ModelForm):

    electricity_consumption = forms.DecimalField(
        min_value=0, decimal_places=2, initial=0
    )
    consumption_unit = forms.ChoiceField(
        choices=ENEERGY_UNIT_CHOICES,
        required=True,
        initial=ENEERGY_UNIT_CHOICES[0],
        error_messages={
            "required": "Please select a Unit.",
            "invalid_choice": "Invalid Unit choice.",
        },
        share_of_renewable_energy=forms.DecimalField(
            min_value=0,
            max_value=1.0,
            max_digits=3,
            decimal_places=2,
            initial=0,
        ),
    )

    class Meta:
        model = HousehodUsages
        # Limit the input fields
        fields = [
            "electricity_consumption",
            "consumption_unit",
        ]

    def clean(self):
        value = self.cleaned_data
        return value
