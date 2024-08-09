from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import VehicleUsagesForm

# Create your views here.


from django.shortcuts import render
from vehicle_usages.models import VehicleUsages


@login_required()
def vehicle_usages_create(request, id=None):
    form = VehicleUsagesForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        item = form.save()
        # flight_distance = form.cleaned_data.get("flight_distance")
        # flight_unit = form.cleaned_data.get("flight_unit")
        # public_transit_distance = form.cleaned_data.get("public_transit_distance")
        # transit_unit = form.cleaned_data.get("transit_unit")
        # item = VehicleUsages.objects.create(
        #     flight_distance=float(flight_distance),
        #     flight_unit=flight_unit,
        #     public_transit_distance=float(public_transit_distance),
        #     transit_unit=transit_unit,
        # )
        context = {
            "created": True,
            "title": "Vehicle Create",
            "item": item,
            "form": form,
        }
    else:
        context = {"created": False, "title": "Vehicle Create", "form": form}
    return render(request, "vehicle_usages/create.html", context)


# def vehicle_usages_create(request, id=None):
#     form = VehicleUsagesForm()
#     if request.method == "POST":
#         form = VehicleUsagesForm(request.POST)
#         if form.is_valid():
#             flight_distance = form.cleaned_data.get("flight_distance")
#             flight_unit = form.cleaned_data.get("flight_unit")
#             public_transit_distance = form.cleaned_data.get("public_transit_distance")
#             transit_unit = form.cleaned_data.get("transit_unit")
#             item = VehicleUsages.objects.create(
#                 flight_distance=float(flight_distance),
#                 flight_unit=flight_unit,
#                 public_transit_distance=float(public_transit_distance),
#                 transit_unit=transit_unit,
#             )
#             context = {
#                 "created": True,
#                 "title": "Vehicle Create",
#                 "item": item,
#                 "form": form,
#             }
#     else:
#         context = {"created": False, "title": "Vehicle Create", "form": form}
#     return render(request, "vehicle_usages/create.html", context)


def vehicle_usages_list(request):
    new_item = VehicleUsages.objects.all()
    context = {"items": new_item, "title": "Vehicle Usages"}
    return render(request, "vehicle_usages/list.html", context)


def vehicle_usages_detail(request, id=None):
    new_item = None
    if id is not None:
        new_item = VehicleUsages.objects.get(id=id)
    context = {"item": new_item, "title": "Vehicle Usages Details"}
    return render(request, "vehicle_usages/details.html", context)
