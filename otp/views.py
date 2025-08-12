
import random
from datetime import timedelta
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import OTP

def login_request(request):
    if request.method == "POST":
        code = "{:06d}".format(random.randint(0, 999999))
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        OTP.objects.create(code=code, session_key=session_key)
        print(f"Generated OTP for session {session_key}: {code}")  # for dev/testing
        return redirect('validate_otp')
    return render(request, 'otp/login.html')

def validate_otp(request):
    error = ""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    latest_otp = OTP.objects.filter(session_key=session_key).order_by('-created_at').first()
    expired = lambda obj: timezone.now() > obj.created_at + timedelta(minutes=5)
    if request.method == "POST":
        entered = request.POST.get('otp')
        if not latest_otp or expired(latest_otp):
            error = "Your code has expired. Please login again."
        elif latest_otp.code != entered:
            error = "Incorrect code. Please try again."
        else:
            request.session['is_authenticated'] = True
            return redirect('main_screen')
    return render(request, 'otp/validate_otp.html', {'error': error})
from django.shortcuts import render

def main_screen(request):
    is_authenticated = request.session.get('is_authenticated', False)
    if not is_authenticated:
        return redirect('login')
    return render(request, 'otp/main_screen.html')
