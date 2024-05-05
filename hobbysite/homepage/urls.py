from django.urls import path

from .views import homepage_test

app_name = "homepage"

urlpatterns = [
    path("home/", homepage_test, name="home"),
]
