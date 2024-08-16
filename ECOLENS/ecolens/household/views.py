from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import HouseholdUsages

# from .forms import VehicleUsagesForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator(login_required, name="dispatch")
class HouseholdUsagesCreateView(SuccessMessageMixin, CreateView):
    model = HouseholdUsages
    # ristrict field input
    fields = [
        "electricity_consumption",
        "electricity_consumption_unit",
        "share_of_renewable_energy",
        "natural_gas_consumption",
        "natural_gas_consumption_unit",
        "heating_oil_consumption",
        "heating_oil_consumption_unit",
        "living_space",
        "living_space_unit",
        "water_consumption",
        "water_consumption_unit",
        "waste_recycling",
        "waste_recycling_unit",
        "waste_incineration",
        "waste_incineration_unit",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("household:household_usages_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Residential Usagescreate"
        context["heading"] = "Residential Usages"
        return context


class HouseholdUsagesListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = HouseholdUsages

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "id")
        new_context = HouseholdUsages.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "Residential Usages list"
        context["heading"] = "Residential Usages list"
        return context


class HouseholdUsagesDetailView(DetailView):
    model = HouseholdUsages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "residential usages"
        return context


class HouseholdUsagesUpdateView(UpdateView):
    model = HouseholdUsages
    fields = [
        "electricity_consumption",
        "electricity_consumption_unit",
        "share_of_renewable_energy",
        "natural_gas_consumption",
        "natural_gas_consumption_unit",
        "heating_oil_consumption",
        "heating_oil_consumption_unit",
        "living_space",
        "living_space_unit",
        "water_consumption",
        "water_consumption_unit",
        "waste_recycling",
        "waste_recycling_unit",
        "waste_incineration",
        "waste_incineration_unit",
    ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("household:household_usages_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update resedantial usages"
        return context


class HouseholdUsagesDeleteView(DeleteView):
    model = HouseholdUsages
    success_url = reverse_lazy("household:household_usages_list")
