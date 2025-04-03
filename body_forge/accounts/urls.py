from django.urls import path

from body_forge.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name="register")
]