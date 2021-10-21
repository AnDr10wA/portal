from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from .models import Profile


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('/')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request, 'register.html', {'register_form':form} )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username} ')
                return redirect("/news")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password.')

    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':form})

def logout_request(request):
    pass