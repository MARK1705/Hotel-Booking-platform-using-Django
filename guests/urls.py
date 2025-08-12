from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_main, name='guests'),
    path('list/', views.guest_list_json, name='guest_list_json'),
    path('add/', views.add_guests, name='add_guests'),
    path('delete/<int:guest_id>/', views.delete_guest, name='delete_guest'),
]
