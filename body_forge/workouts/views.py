from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from body_forge.exercises.models import MuscleGroup, Exercise
from body_forge.workouts.forms import WorkoutCreateForm
from body_forge.workouts.models import Workout


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutCreateForm
    template_name = "workouts/workout-create-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_exercises"] = Exercise.objects.filter(user=self.request.user)

        return context