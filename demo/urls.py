
from os import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.SignUpView.as_view(), name='starting_page'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.Profile.as_view(), name='profile')
]
