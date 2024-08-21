from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# from .forms import VehicleUsagesForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
from .models import General


# @method_decorator(login_required, name="dispatch")
class GeneralCreateView(SuccessMessageMixin, CreateView):
    model = General
    # ristrict field input
    fields = [
        "num_people",
    ]
    # fields = "__all__"

    success_url = reverse_lazy("general:general_list")
    # template_name = "books/update.html"
    success_message = "Created successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        context["heading"] = "No of People"
        return context


class GeneralListView(ListView):
    paginate_by = 5  # Adjust the number of items per page
    model = General

    def get_queryset(self):
        # '-' indicates descending order
        # order = self.request.GET.get("orderby", "-updated_at")
        order = self.request.GET.get("orderby", "-updated_at")
        new_context = General.objects.order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        # page = context["page"]
        # Add additional context variables as needed
        context["title"] = "list"
        context["heading"] = "General list"
        return context


class GeneralDetailView(DetailView):
    model = General

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail"
        context["heading"] = "Other Usages"
        return context


class GeneralUpdateView(UpdateView):
    model = General
    fields = [
        "num_people",
    ]
    template_name_suffix = "_update_form"
    # success_url = reverse_lazy("other:other_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["heading"] = "Update No Of people"
        return context

    def get_success_url(self):
        messages.success(self.request, "Updated successfully")
        return reverse_lazy("general:general_list")


class GeneralDeleteView(SuccessMessageMixin, DeleteView):
    model = General

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy("general:general_list")
