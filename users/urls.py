from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('api/users/', views.UserCreate.as_view(), name='account-create'),
]