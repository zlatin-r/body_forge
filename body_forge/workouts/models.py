from django.contrib.auth import get_user_model
from django.db import models

from body_forge.exercises.models import Exercise, MuscleGroup
from body_forge.workouts.workout_type_choices import WorkoutTypes

UserModel = get_user_model()


class Workout(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='workouts'
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )
    workout_type = models.CharField(
        max_length=10,
        choices=WorkoutTypes
    )
    date = models.DateField(
        auto_now_add=True
    )
    notes = models.TextField(
        blank=True
    )
    exercises = models.ManyToManyField(
        to=Exercise,
        blank=True
    )
