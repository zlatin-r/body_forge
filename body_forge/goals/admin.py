from django.contrib import admin

from body_forge.goals.models import UserGoal


# Register your models here.
@admin.register(UserGoal)
class UserGoalAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "goal_type",
        "description",
        "target_value",
        "target_date",
        "is_achieved",
        "created_at",
    )
