from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from body_forge.workouts.forms import WorkoutCreateForm
from body_forge.workouts.models import Workout


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutCreateForm
    template_name = "workouts/workout-create-page.html"


