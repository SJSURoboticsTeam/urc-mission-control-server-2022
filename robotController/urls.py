from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("robotServer", include("robotServer.urls"))
    # path("results", views.results, name="results"),
    # path("register", views.register, name="register"),
    # path("login", views.login, name="login")
]