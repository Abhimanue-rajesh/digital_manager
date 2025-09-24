from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from creative.forms import CreativeForm
from creative.models import Creative


class CreativeListView(LoginRequiredMixin, ListView):
    model = Creative
    template_name = "creative/list_creatives.html"
    context_object_name = "creatives"
    ordering = ["-posting_date"]


class CreativeCreateView(LoginRequiredMixin, CreateView):
    model = Creative
    form_class = CreativeForm
    template_name = "creative/create_update_form.html"
    success_url = reverse_lazy("list_creatives")  # redirect to your list view


class CreativeUpdateView(LoginRequiredMixin, UpdateView):
    model = Creative
    form_class = CreativeForm
    template_name = "creative/create_update_form.html"
    success_url = reverse_lazy("list_creatives")


class CreativeDetailView(LoginRequiredMixin, DetailView):
    model = Creative
    template_name = "creative/detail_creative.html"
    context_object_name = "creative"
