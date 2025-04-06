from django import forms

from body_forge.muscle_groups.models import MuscleGroup


class MuscleGroupCreateForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = '__all__'
