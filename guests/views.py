
from django.shortcuts import render
from django.http import JsonResponse
from .models import Guest
import json
from django.views.decorators.csrf import csrf_exempt

def guest_main(request):
    return render(request, 'guests/guest_main.html')

def guest_list_json(request):
    session_key = request.session.session_key or request.session.create()
    guests = Guest.objects.filter(session_key=session_key)
    data = [
        {"id": g.id, "name": g.name, "contact": g.contact, "email": g.email}
        for g in guests
    ]
    return JsonResponse({"guests": data})

@csrf_exempt
def add_guests(request):
    if request.method == "POST":
        session_key = request.session.session_key or request.session.create()
        data = json.loads(request.body.decode())
        guests_in = data.get("guests", [])
        created = []
        for guest_data in guests_in:
            name = guest_data.get('name', '').strip()
            contact = guest_data.get('contact', '')
            email = guest_data.get('email', '')
            if not name:
                return JsonResponse({"error": "Guest name required."}, status=400)
            guest = Guest.objects.create(
                name=name, contact=contact, email=email, session_key=session_key
            )
            created.append({"id": guest.id, "name": name, "contact": contact, "email": email})
        return JsonResponse({"guests": created})
    return JsonResponse({"error": "POST required."}, status=405)

@csrf_exempt
def delete_guest(request, guest_id):
    session_key = request.session.session_key or request.session.create()
    try:
        guest = Guest.objects.get(id=guest_id, session_key=session_key)
        guest.delete()
        return JsonResponse({"ok": True})
    except Guest.DoesNotExist:
        return JsonResponse({"ok": False}, status=404)
