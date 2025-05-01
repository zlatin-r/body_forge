from django import forms

from body_forge.exercises.models import Exercise, ExerciseLog


class ExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'name',
            'description',
            'primary_muscle_group',
            'secondary_muscle_groups',
            'exercise_type',
            'sets',
            'weight',
            'repetitions',
            'rest_time'
        ]
        labels = {
            'name': 'Exercise Name',
            'description': 'Description',
            'primary_muscle_group': 'Primary Muscle Group',
            'secondary_muscle_groups': 'Secondary Muscle Group',
            'exercise_type': 'Exercise Type',
            'sets': 'Sets',
            'weight': 'Weight',
            'repetitions': 'Repetitions',
            'rest_time': 'Rest Time',
        }


class ExerciseLogForm(forms.ModelForm):
    class Meta:
        model = ExerciseLog
        fields = ['sets', 'reps', 'weight']  # Customize field names
