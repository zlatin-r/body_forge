from django.contrib.auth import get_user_model
from django.db import models

from body_forge.exercises.exercise_type_choices import ExerciseTypes

UserModel = get_user_model()


class Exercise(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="exercise"
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        blank=True
    )
    primary_muscle_group = models.ForeignKey(
        to='muscle_groups.MuscleGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name='primary_muscle_groups'
    )
    secondary_muscle_groups = models.ManyToManyField(
        to='muscle_groups.MuscleGroup',
        blank=True,
        related_name='secondary_muscle_groups'
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


class ExerciseLog(models.Model):
    workout = models.ForeignKey(
        to='workouts.Workout',
        on_delete=models.CASCADE,
        related_name='logs'
    )
    exercise = models.ForeignKey(
        to='exercises.Exercise',
        on_delete=models.CASCADE
    )
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField()