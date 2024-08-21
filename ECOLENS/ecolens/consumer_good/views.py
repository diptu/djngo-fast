from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import ConsumerGood

# from .forms import VehicleUsagesForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator(login_required, name="dispatch")
class ConsumerGoodsCreateView(SuccessMessageMixin, CreateView):
    model = ConsumerGood
    # ristrict field input
    fields = [
        "clothing",
        "appliances",
        "pharmaceuticals",
        "furniture",
        "hospitality",
        "services",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("consumer_good:consumer_good_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "create"
        context["heading"] = "Consumer Gooods and Service"
        return context


class ConsumerGoodsListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = ConsumerGood

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "id")
        new_context = ConsumerGood.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "Consumer Goods list"
        context["heading"] = "Consumer Gooods and Service list"
        return context


class ConsumerGoodsDetailView(DetailView):
    model = ConsumerGood

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "Consumer Goods and Services"
        return context


class HouseholdUsagesUpdateView(UpdateView):
    model = ConsumerGood
    fields = [
        "clothing",
        "appliances",
        "pharmaceuticals",
        "furniture",
        "hospitality",
        "services",
    ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("consumer_good:consumer_good_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update Consumer Goods and Services"
        return context


class ConsumerGoodDeleteView(DeleteView):
    model = ConsumerGood
    success_url = reverse_lazy("consumer_good:consumer_good_list")
