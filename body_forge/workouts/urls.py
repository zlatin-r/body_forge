from django.urls import path

from body_forge.workouts import views

urlpatterns = [
    path('create/', views.WorkoutCreateView.as_view(), name="create-workout"),
    path('details/<int:workout_id>/', views.WorkoutDetailView.as_view(), name="details-workout"),
    path('delete/<int:pk>/', views.WorkoutDeleteView.as_view(), name="delete-workout"),
]
