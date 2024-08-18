from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Emission

# from .forms import VehicleUsagesForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


# @method_decorator(login_required, name="dispatch")
class EmissionCreateView(SuccessMessageMixin, CreateView):
    model = Emission
    # ristrict field input
    fields = [
        "vehicle_usages",
        "household_usages",
        "food_consumption",
        "unit",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("carbon_footprint:carbon_footprint_list")
    # template_name = "books/create.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carbon Footprint create"
        context["heading"] = "Carbon Footprint"
        return context


class EmissionListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = Emission

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "-updated_at")
        new_context = Emission.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "CO2 foootprint list"
        context["heading"] = "CO2 footprint list"
        return context


class EmissionDetailView(DetailView):
    model = Emission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "CO2 footprint"
        return context


class EmissionUpdateView(UpdateView):
    model = Emission
    fields = [
        "vehicle_usages",
        "household_usages",
        "food_consumption",
        "unit",
    ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("carbon_footprint:carbon_footprint_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update food consumption"
        return context


class EmissionDeleteView(SuccessMessageMixin, DeleteView):
    model = Emission

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy("carbon_footprint:carbon_footprint_list")
