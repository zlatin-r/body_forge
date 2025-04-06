from django import forms

from body_forge.exercises.models import Exercise


class ExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ("user",)
