from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from body_forge.muscle_groups.forms import MuscleGroupCreateForm
from body_forge.muscle_groups.models import MuscleGroup


class MuscleGroupCreateView(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = MuscleGroupCreateForm
    template_name = "muscle_groups/muscle-group-create-page.html"
    success_url = reverse_lazy("create-exercise")
