from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Emission
from household.models import HouseholdUsages

# from .forms import VehicleUsagesForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


from vehicle_usages.models import VehicleUsages
from household.models import HouseholdUsages
from food.models import FoodConsumption
from general.models import General
from consumer_good.models import ConsumerGood
from other.models import OtherUsages


# @method_decorator(login_required, name="dispatch")
class EmissionCreateView(SuccessMessageMixin, CreateView):
    model = Emission
    # ristrict field input

    fields = [
        "vehicle_usages",
        "household_usages",
        "food_consumption",
        "consumer_good",
        "other_uages",
        "unit",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("carbon_footprint:carbon_footprint_list")
    success_message = "Created successfully!"

    def get(self, request, *args, **kwargs):
        vehicle_count = VehicleUsages.objects.count()
        household_count = HouseholdUsages.objects.count()
        food_count = FoodConsumption.objects.count()
        general_count = General.objects.count()
        consumer_goods_count = ConsumerGood.objects.count()
        other_count = OtherUsages.objects.count()

        if vehicle_count <= 0:
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("vehicle_usages:create"))
        elif household_count <= 0:
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("household:household_usages_create"))
        elif food_count <= 0:
            if general_count > 0:
                messages.warning(
                    self.request, "Your object has need to be created yet."
                )
            return redirect(reverse_lazy("food:food_consumption_create"))
        elif consumer_goods_count <= 0:
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("consumer_good:consumer_good_create"))
        elif other_count <= 0:
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("other:other_create"))

        return super().get(request, *args, **kwargs)

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
        "consumer_good",
        "miscellaneous",
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
