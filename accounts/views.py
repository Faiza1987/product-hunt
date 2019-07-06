from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm-password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken.'})

            except User.DoesNotExist:
                new_user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, new_user)

                return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match.'})

    else: # User already has an account (GET existing user and prevent signup)
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/signup.html')