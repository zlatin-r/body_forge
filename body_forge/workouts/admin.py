from django.contrib import admin

from body_forge.workouts.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "workout_type",
        "date",
        "notes",
    )

#
# @admin.register(WorkoutExercise)
# class WorkoutExerciseAdmin(admin.ModelAdmin):
#     list_display = (
#         "exercise",
#         "order",
#         "notes"
#     )
#
# @admin.register(ExerciseSet)
# class ExerciseSetAdmin(admin.ModelAdmin):
#     list_display = (
#         "set_number",
#         "weight",
#         "reps",
#         "duration",
#         "distance",
#         "rpe",
#     )