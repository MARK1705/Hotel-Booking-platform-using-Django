
from django.shortcuts import render
from .models import Hotel

def search_hotels(request):
    city = request.GET.get('city', '').strip()
    hotel_name = request.GET.get('hotel_name', '').strip()
    hotels = Hotel.objects.all()
    if city:
        hotels = hotels.filter(city__iexact=city)
    if hotel_name:
        hotels = hotels.filter(name__icontains=hotel_name)
    return render(request, 'hotel/search.html', {
        'hotels': hotels,
        'city': city,
        'hotel_name': hotel_name,
    })
