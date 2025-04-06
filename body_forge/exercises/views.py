from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from body_forge.exercises.forms import ExerciseCreateForm
from body_forge.exercises.models import Exercise


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseCreateForm
    template_name = "exercises/exercise-create-page.html"
    success_url = reverse_lazy("create-workout")