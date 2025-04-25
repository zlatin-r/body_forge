from django.urls import path, include

from body_forge.workouts import views

urlpatterns = [
    path('create/', views.WorkoutCreateView.as_view(), name="create-workout"),
    path('<slug:workout_slug>/', include([
        path('details/', views.DetailView.as_view(), name="details-workout")
    ])),
    # path('details/<int:workout_id>/', views.WorkoutDetailView.as_view(), name="details-workout"),
]