from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# from .forms import VehicleUsagesForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from general.models import General

# Create your views here.
from .models import OtherUsages


# @method_decorator(login_required, name="dispatch")
class OtherCreateView(SuccessMessageMixin, CreateView):
    model = OtherUsages
    # ristrict field input
    fields = ["education", "activities", "general"]
    # fields = "__all__"

    success_url = reverse_lazy("other:other_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get(self, request, *args, **kwargs):
        if not General.objects.count():
            messages.warning(self.request, "Your object has need to be created yet.")
            return redirect(reverse_lazy("general:general_create"))

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        context["heading"] = "Other Create"
        return context


class OtherListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = OtherUsages

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "-updated_at")
        new_context = OtherUsages.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "list"
        context["heading"] = "Other Usages list"
        return context


class OtherDetailView(DetailView):
    model = OtherUsages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "Other Usages"
        return context


class OtherUpdateView(UpdateView):
    model = OtherUsages
    fields = [
        "education",
        "activities",
        "general",
    ]
    template_name_suffix = "_update_form"
    # success_url = reverse_lazy("other:other_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update Other Usages"
        return context

    def get_success_url(self):
        messages.success(self.request, "Updated successfully")
        return reverse_lazy("other:other_list")


class OtherDeleteView(SuccessMessageMixin, DeleteView):
    model = OtherUsages

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy("other:other_list")
