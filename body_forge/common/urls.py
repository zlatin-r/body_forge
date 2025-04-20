from django.urls import path

from body_forge.common import views
from body_forge.common.views import index

urlpatterns = [
    path('', views.HomePage.as_view(), name="home-page"),
]