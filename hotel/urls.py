from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_hotels, name='hotel_search'),
]
