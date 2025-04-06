from django.contrib import admin

from body_forge.exercises.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "primary_muscle_group",
        "exercise_type",
        "equipment_needed"
    )
