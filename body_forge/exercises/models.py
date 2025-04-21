from django.contrib.auth import get_user_model
from django.db import models

from body_forge.exercises.exercise_type_choices import ExerciseTypes
from body_forge.muscle_groups.models import MuscleGroup

UserModel = get_user_model()


class Exercise(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="exercise"
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        blank=True
    )
    primary_muscle_group = models.ForeignKey(
        to=MuscleGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name='primary_exercises'
    )
    secondary_muscle_groups = models.ManyToManyField(
        to=MuscleGroup,
        blank=True,
        related_name='secondary_exercises'
    )
    exercise_type = models.CharField(
        max_length=11,
        choices=ExerciseTypes,
        default='STRENGTH'
    )
    sets = models.PositiveIntegerField(
        default=0
    )
    weight = models.PositiveIntegerField(
        default=0
    )
    repetitions = models.PositiveIntegerField(
        default=0
    )
    rest_time = models.FloatField(
        default=0
    )

    def __str__(self):
        return self.name
