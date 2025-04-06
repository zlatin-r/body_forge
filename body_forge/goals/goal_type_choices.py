from django.db import models


class GoalTypeChoices(models.TextChoices):
    STRENGTH = "Strength", "Strength"
    ENDURANCE = "Endurance", "Endurance"
    Weight = "Weight", "Weight"
    OTHER = "Other", "Other"
