from django.views.generic import ListView

from body_forge.workouts.models import Workout


class HomePage(ListView):
    model = Workout
    template_name = 'common/home-page.html'
    context_object_name = 'all_workouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.prefetch_related('exercises')
