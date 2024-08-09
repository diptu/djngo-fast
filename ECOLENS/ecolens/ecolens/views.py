"""Render HTML"""

from django.shortcuts import render
from vehicle_usages.models import VehicleUsages


def home(request):
    new_item = VehicleUsages.objects.all()
    context = {"items": new_item, "title": "Home"}
    return render(request, "home.html", context)


def about(request):
    context = {"title": "About"}
    return render(request, "about.html", context)
