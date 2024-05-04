from django.urls import path

from .views import ProfileCreateView

app_name = "accounts"

urlpatterns = [
    path("register/", ProfileCreateView.as_view(), name="register"),
]
