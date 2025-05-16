# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'home/login.html')

@login_required
def dashboard_view(request):
    students = Student.objects.all()
    return render(request, 'dashboard/dashboard.html', {'students': students})

def logout_view(request):
    logout(request)
    return redirect('login')
