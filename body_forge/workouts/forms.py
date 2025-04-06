from django import forms

from body_forge.workouts.models import Workout


class WorkoutCreateForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["workout_type", "notes", "muscle_groups_trained"]