from django import forms

from body_forge.workouts.models import Workout


class WorkoutCreateForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["workout_type", "notes"]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

class WorkoutDeleteForm(forms.Form):  # Optional: Create a confirmation form
    confirm_delete = forms.BooleanField(
        label='Confirm Deletion',
        required=True,
        widget=forms.HiddenInput(attrs={'value': True})  # Add a hidden confirmation
    )
