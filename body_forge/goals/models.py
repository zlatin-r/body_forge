from django.contrib.auth import get_user_model
from django.db import models

from body_forge.goals.goal_type_choices import GoalTypeChoices

UserModel = get_user_model()


class UserGoal(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    goal_type = models.CharField(
        max_length=9,
        choices=GoalTypeChoices
    )
    description = models.TextField(
    )
    target_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True)
    target_date = models.DateField(
    )
    is_achieved = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username}'s {self.goal_type} goal"
