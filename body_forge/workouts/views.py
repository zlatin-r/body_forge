from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from body_forge.exercises.models import MuscleGroup, Exercise
from body_forge.workouts.forms import WorkoutCreateForm
from body_forge.workouts.models import Workout


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutCreateForm
    template_name = "workouts/workout-create-page.html"
    success_url = reverse_lazy("home-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_exercises"] = Exercise.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        # Set the user before saving
        form.instance.user = self.request.user
        # Save the workout
        response = super().form_valid(form)
        # Add selected exercises
        exercise_ids = self.request.POST.getlist('exercises')
        if exercise_ids:
            # Ensure only the user's exercises are added (security)
            exercises = Exercise.objects.filter(id__in=exercise_ids, user=self.request.user)
            self.object.exercises.set(exercises)
        return response