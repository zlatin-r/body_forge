from django.urls import path

from body_forge.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home-page"),
]
