from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(requests):
    return render(requests, 'home/welcome.html')

def dashboard(requests):
    return render(requests, 'home/dashboard.html')

def country(requests):
    return render(requests, 'home/country.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password_confirm = request.POST['password_confirm']
        print(f"username {username} password {password}")
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('login')  # Replace 'home' with the name of the URL you want to redirect to after registering.
        else:
            messages.error(request, 'Passwords do not match')
            
    return render(request, 'home/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"username {username} password {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'home/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')