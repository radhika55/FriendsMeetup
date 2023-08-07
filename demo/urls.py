
from os import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.SignUpAPIView.as_view(), name='starting_page'),
    path('login/', views.UserLoginApi.as_view(), name='login'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile')
]
