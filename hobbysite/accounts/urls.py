from django.urls import path

from .views import UserCreateView, dashboard

app_name = "accounts"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("dashboard/", dashboard, name="dashboard"),
]
