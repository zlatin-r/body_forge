from django.contrib.auth.views import LogoutView
from django.urls import path

from body_forge.accounts import views

urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.AppUserRegisterView.as_view(), name="register"),
]
