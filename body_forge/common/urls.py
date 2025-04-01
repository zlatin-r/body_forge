from django.urls import path

from body_forge.common.views import index

urlpatterns = [
    path('', index, name="index"),
]