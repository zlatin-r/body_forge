from django.db import models

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
