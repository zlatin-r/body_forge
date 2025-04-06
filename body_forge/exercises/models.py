from django.db import models

from body_forge.exercises.exercise_type_choices import ExerciseTypes


class MuscleGroup(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        blank=True
    )
    primary_muscle_group = models.ForeignKey(
        MuscleGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name='primary_exercises'
    )
    secondary_muscle_groups = models.ManyToManyField(
        MuscleGroup,
        blank=True,
        related_name='secondary_exercises'
    )
    exercise_type = models.CharField(
        max_length=11,
        choices=ExerciseTypes,
        default='STRENGTH'
    )
    equipment_needed = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name
