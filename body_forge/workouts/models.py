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


    def __str__(self):
        return f"{self.user.username}'s workout on {self.date}"

    class Meta:
        ordering = ['-date']


# class WorkoutExercise(models.Model):
#     workout = models.ForeignKey(
#         to=Workout,
#         on_delete=models.CASCADE,
#         related_name='exercises'
#     )
#     exercise = models.ForeignKey(
#         to=Exercise,
#         on_delete=models.CASCADE
#     )
#     order = models.PositiveIntegerField(
#         default=0
#     )
#     notes = models.TextField(
#         blank=True
#     )
#
#     class Meta:
#         ordering = ['order']
#
#     def __str__(self):
#         return f"{self.exercise.name} in {self.workout}"


# class ExerciseSet(models.Model):
#     workout_exercise = models.ForeignKey(
#         WorkoutExercise,
#         on_delete=models.CASCADE,
#         related_name='sets'
#     )
#     set_number = models.PositiveIntegerField(
#     )
#     weight = models.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         null=True,
#         blank=True
#     )
#     reps = models.PositiveIntegerField(
#     )
#     duration = models.DurationField(
#         null=True,
#         blank=True
#     )  # For cardio/timed exercises
#     distance = models.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         help_text="Distance in meters"
#     )
#     rpe = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(10)
#         ],
#         help_text="Rate of Perceived Exertion (1-10)"
#     )
#
#     class Meta:
#         ordering = ['set_number']
#         unique_together = ('workout_exercise', 'set_number')
#
#     def __str__(self):
#         return f"Set {self.set_number} of {self.workout_exercise}"
