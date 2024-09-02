from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import FoodConsumption

# from .forms import VehicleUsagesForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from general.models import General

from django.db.models.signals import pre_save
from django.dispatch import receiver


# @method_decorator(login_required, name="dispatch")
class FoodConsumptionCreateView(SuccessMessageMixin, CreateView):
    model = FoodConsumption
    # ristrict field input
    fields = [
        "diet_type",
        "consumption_level",
        "level_of_wastage",
        "consumption_unit",
        "general",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("food:food_consumption_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get(self, request, *args, **kwargs):
        # Check if a condition is met and redirect if necessary

        if not General.objects.count():
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("general:general_create"))

        return super().get(request, *args, **kwargs)

    # def render_to_response(self, context, **response_kwargs):
    #     general = General.objects.count()
    #     print(f"general:{general}")
    #     if general <= 0:
    #         print("general is empty!")
    #         messages.success(self.request, "Your object has need to be created first.")
    #         return redirect(reverse_lazy("general:general_create"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Food Consumption create"
        context["heading"] = "Food Consumption"
        return context


class FoodConsumptionListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = FoodConsumption

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "id")
        new_context = FoodConsumption.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "Food Consumption list"
        context["heading"] = "Food Consumption list"
        return context


class FoodConsumptionDetailView(DetailView):
    model = FoodConsumption

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "Food Consumption"
        return context


class FoodConsumptionUpdateView(UpdateView):
    model = FoodConsumption
    fields = [
        "diet_type",
        "consumption_level",
        "level_of_wastage",
        "consumption_unit",
        "general",
    ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("food:food_consumption_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update food consumption"
        return context


class FoodConsumptionDeleteView(SuccessMessageMixin, DeleteView):
    model = FoodConsumption

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy("food:food_consumption_list")
