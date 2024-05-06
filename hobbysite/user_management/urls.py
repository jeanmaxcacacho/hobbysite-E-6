from django.urls import path

from .views import UserCreateView, dashboard

app_name = "user_management"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("dashboard/", dashboard, name="dashboard"),
]