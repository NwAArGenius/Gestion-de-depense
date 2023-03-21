from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages

User = get_user_model()

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('')
        user = User.objects.create_user(username=username, email=email, 
                                        password=password)
        login(request, user)
        return redirect("home")
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email ou mot de pass non valide')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
        