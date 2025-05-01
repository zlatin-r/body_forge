from django.urls import path

from body_forge.exercises import views

urlpatterns = [
    path('create/', views.ExerciseCreateView.as_view(), name="create-exercise"),
    path('exercise/<int:exercise_id>/start/', views.start_exercise, name='start-exercise'),
]
