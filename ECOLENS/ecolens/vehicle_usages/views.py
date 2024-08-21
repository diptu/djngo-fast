from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import VehicleUsages
from .forms import VehicleUsagesForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from django.contrib.auth.decorators import login_required

# Create Class based views here.


# @method_decorator(login_required, name="dispatch")
class VehicleUsagesCreateView(SuccessMessageMixin, CreateView):
    # form_class = VehicleUsagesForm
    model = VehicleUsages
    # ristrict field input
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
    # fields = "__all__"

    success_url = reverse_lazy("vehicle_usages:vihicle_usages_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "vehicle usages create"
        context["heading"] = "create vehicle usages"
        return context


class VehicleUsagesListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = VehicleUsages

    def get_queryset(self):
        # '-' indicates descending order
        order = self.request.GET.get("orderby", "-updated_at")
        new_context = VehicleUsages.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "vehicle usages list"
        context["heading"] = "vehicle usages list"
        return context


class VehicleUsagesDetailView(DetailView):
    model = VehicleUsages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "vehicle usages"
        return context


class VehicleUsagesUpdateView(UpdateView):
    model = VehicleUsages
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
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update vehicle usages"
        return context


class VehicleUsagesDeleteView(DeleteView):
    model = VehicleUsages
    success_url = reverse_lazy("vehicle_usages:vihicle_usages_list")
