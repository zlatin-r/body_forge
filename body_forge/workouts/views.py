from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

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
        form.instance.user = self.request.user
        response = super().form_valid(form)
        exercise_ids = self.request.POST.getlist('exercises')

        if exercise_ids:
            exercises = Exercise.objects.filter(id__in=exercise_ids, user=self.request.user)
            self.object.exercises.set(exercises)
        return response


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workouts/workout-details-page.html'
    context_object_name = 'workout'
    pk_url_kwarg = 'workout_id'
