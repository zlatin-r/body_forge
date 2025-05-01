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
    context_object_name = "exercise"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user here
        return super().form_valid(form)


from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise, Workout
from .forms import ExerciseLogForm

def start_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    workout_id = request.GET.get('workout_id')
    workout = get_object_or_404(Workout, pk=workout_id)

    if request.method == 'POST':
        form = ExerciseLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.exercise = exercise
            log.workout = workout
            log.save()
            return redirect('create-workout')  # or the same page if multi-exercise entry
    else:
        form = ExerciseLogForm()

    return render(request, 'exercises/start-exercise.html', {
        'exercise': exercise,
        'form': form,
    })
