from django.urls import path

from body_forge.muscle_groups import views

urlpatterns = [
    path('create/', views.MuscleGroupCreateView.as_view(), name="create-muscle-group"),
]