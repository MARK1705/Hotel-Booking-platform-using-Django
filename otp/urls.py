from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name='login'),
    path('validate/', views.validate_otp, name='validate_otp'),
    path('main/', views.main_screen, name='main_screen'),
]