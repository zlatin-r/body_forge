from django.urls import path

from body_forge.exercises import views

urlpatterns = [
    path('create/', views.ExerciseCreateView.as_view(), name="create-exercise")
]