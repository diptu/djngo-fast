from typing import Any
from django import forms
from .models import VehicleUsages

DISTANCE_CHOICES = (
    ("Km", "Kilometer"),
    ("Mi", "Mile"),
)


class VehicleUsagesForm(forms.ModelForm):
    class Meta:
        model = VehicleUsages
        # Limit the input fields
        fields = [
            "flight_distance",
            "flight_unit",
            "public_transit_distance",
            "transit_unit",
            "num_of_gasolin_cars",
            "num_of_diesel_cars",
            "num_of_electric_cars",
            "num_of_hybrid_cars",
            "gasoline_car_driven",
            "gasolin_car_unit",
            "diesel_car_driven",
            "diesel_car_unit",
            "electric_car_driven",
            "electric_car_unit",
            "hybrid_car_driven",
            "hybrid_car_unit",
        ]

    def clean(self):
        # data = self.cleaned_data  # a dictionary
        value = self.cleaned_data
        # if value not in [choice[0] for choice in DISTANCE_CHOICES]:
        #     raise ValueError("Invalid  Unit. Choose from Km or Mi.")
        return value


# class CO2EmissionUnit(forms.ChoiceField):
#     TCO2EQ = "tCO2eq", "Tons of Carbon Dioxide Equivalent"
#     TCO2EQ_PER_KM = "tCO2eq/km", "Tons of Carbon Dioxide Equivalent per Kilometer"


# class VehicleUsagesForm(forms.Form):
#     flight_distance = forms.FloatField(
#         label="Flight Flown per year",
#         min_value=0,
#         required=True,
#         initial=0,
#     )
#     flight_unit = forms.ChoiceField(
#         required=False,
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#     )

#     public_transit_distance = forms.FloatField(
#         label="Public Transit usages per year", min_value=0, required=True, initial=0
#     )
#     transit_unit = forms.ChoiceField(
#         required=False,
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#     )
#     num_of_gasolin_cars = forms.IntegerField(
#         label="No of gasolin car owned", min_value=0, initial=0
#     )
#     num_of_diesel_cars = forms.IntegerField(
#         label="No of Diesel car owned", min_value=0, initial=0
#     )
#     num_of_electric_cars = forms.IntegerField(
#         label="No of Electric car owned", min_value=0, initial=0
#     )
#     num_of_hybrid_cars = forms.IntegerField(
#         label="No of HYbrid car owned", min_value=0, initial=0
#     )

#     gasoline_car_driven = forms.FloatField(initial=0, label="Gasoline car driven")
#     gasolin_car_unit = forms.ChoiceField(
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#         label="Gasoline car driven unit",
#     )
#     diesel_car_driven = forms.FloatField(initial=0, label="Diesel car driven")
#     diesel_car_unit = forms.ChoiceField(
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#         label="Diesel car driven unit",
#     )

#     electric_car_driven = forms.FloatField(initial=0, label="Electric car driven")
#     electric_car_unit = forms.ChoiceField(
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#         label="Electric car driven Unit",
#     )

#     hybrid_car_driven = forms.FloatField(initial=0, label="Hybrid car driven")
#     hybrid_car_unit = forms.ChoiceField(
#         choices=DISTANCE_CHOICES,
#         initial=DISTANCE_CHOICES[0],
#         label="Hybrid car driven Unit",
#     )

#     # def clean_flight_distance(self):
#     #     cleaned_data = self.cleaned_data  # a dictionary
#     #     flight_distance = cleaned_data.get("flight_distance")
#     #     return flight_distance

#     def clean(self):
#         cleaned_data = self.cleaned_data  # a dictionary

#         # flight_distance = cleaned_data.get("flight_distance")
#         # if flight_distance is None:
#         #     raise forms.ValidationError("Distance cannot be empty or negative ")
#         return cleaned_data
