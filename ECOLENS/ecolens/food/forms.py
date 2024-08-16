from django import forms
from .models import FoodConsumption

DIET_CATEGORY_CHOICES = (
    ("VI", "Vegan"),
    ("VG", "Vegetarian"),
    ("FL", "Flexitarian"),
    ("OM", "Omnivore"),
)

EMISSION_CHOICES = ("TCO2_Y", "tCO2equ/year")


class HouseholdeUsagesForm(forms.ModelForm):

    diet_type = forms.ChoiceField(
        choices=DIET_CATEGORY_CHOICES,
        required=True,
        initial=DIET_CATEGORY_CHOICES[0],
        error_messages={
            "required": "Please select a Unit.",
            "invalid_choice": "Invalid Unit choice.",
        },
    )
    consumption_level = (
        forms.DecimalField(
            min_value=0,
            max_value=1.0,
            max_digits=3,
            decimal_places=2,
            initial=0,
        ),
    )
    consumption_unit = forms.ChoiceField(
        choices=EMISSION_CHOICES,
        required=True,
        initial=EMISSION_CHOICES[0],
        error_messages={
            "required": "Please select a Unit.",
            "invalid_choice": "Invalid Unit choice.",
        },
    )

    class Meta:
        model = FoodConsumption
        # Limit the input fields
        fields = [
            "diet_type",
            "consumption_level",
            "level_of_wastage",
            "consumption_unit",
        ]

    def clean(self):
        value = self.cleaned_data
        return value
