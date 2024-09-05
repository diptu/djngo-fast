from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Transport
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
class TransportationCreateView(SuccessMessageMixin, CreateView):
    # form_class = VehicleUsagesForm
    model = Transport
    # ristrict field input
    fields = [
        "flight_distance",
        "flight_unit",
        "public_transit_distance",
        "transit_unit",
        "company_num_of_gasolin_cars",
        "company_num_of_diesel_cars",
        "company_num_of_electric_cars",
        "company_num_of_hybrid_cars",
        "company_gasoline_car_driven",
        "staff_gasoline_car_driven",
        "gasolin_car_unit",
        "company_diesel_car_driven",
        "staff_diesel_car_driven",
        "diesel_car_unit",
        "company_electric_car_driven",
        "staff_electric_car_driven",
        "electric_car_unit",
        "company_hybrid_car_driven",
        "staff_hybrid_car_driven",
        "hybrid_car_unit",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("travel:travel_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Transportation create"
        context["heading"] = "Transportation Usages Create"
        return context


class TransportationListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = Transport

    def get_queryset(self):
        # '-' indicates descending order
        order = self.request.GET.get("orderby", "-updated_at")
        new_context = Transport.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "Transportation  list"
        context["heading"] = "Transportation list"
        return context


class TransportationDetailView(DetailView):
    model = Transport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "Transportation usages"
        return context


class TransportationUpdateView(UpdateView):
    model = Transport
    fields = [
        "flight_distance",
        "flight_unit",
        "public_transit_distance",
        "transit_unit",
        "company_num_of_gasolin_cars",
        "company_num_of_diesel_cars",
        "company_num_of_electric_cars",
        "company_num_of_hybrid_cars",
        "company_gasoline_car_driven",
        "staff_gasoline_car_driven",
        "gasolin_car_unit",
        "company_diesel_car_driven",
        "staff_diesel_car_driven",
        "diesel_car_unit",
        "company_electric_car_driven",
        "staff_electric_car_driven",
        "electric_car_unit",
        "company_hybrid_car_driven",
        "staff_hybrid_car_driven",
        "hybrid_car_unit",
    ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("travel:travel_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update Transportaion usages"
        return context


class TransportationDeleteView(DeleteView):
    model = Transport
    success_url = reverse_lazy("travel:travel_list")
