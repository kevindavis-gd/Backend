from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('createUser/', views.UserCreate.as_view(), name='account-create'),
]