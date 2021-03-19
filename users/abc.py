from django.contrib import admin
from django.urls import path, include
from .router import router
from . import views

urlpatterns = [
    path('register', view.register, name="register"),
]
