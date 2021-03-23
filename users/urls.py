from django.conf.urls import url
from . import views
from django.urls import path, include
# used to obtain token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('createUser/', views.UserCreate.as_view(), name='account-create'),
    path('login/', obtain_auth_token, name='obtain-token'),
]