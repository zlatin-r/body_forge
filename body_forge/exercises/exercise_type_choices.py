from django.db import models


class ExerciseTypes(models.TextChoices):
    STRENGTH = 'Strength', 'Strength'
    CARDIO = 'Cardio', 'Cardio'
    FLEXIBILITY = "Flexibility", "Flexibility"
