from django.urls import path

from body_forge.workouts import views

urlpatterns = [
    path('create/', views.WorkoutCreateView.as_view(), name="create-workout"),
]