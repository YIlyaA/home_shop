from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']    
            password = request.POST['password']    
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Now you are log in!")
                return HttpResponseRedirect(reverse('main:index'))  # Функция reverse преобразует 'main:index' в url и перенаправляет 
    else:
        form = UserLoginForm()        

    
    context = {
        'title': 'Home - authorisation',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, registration was successful")
            return HttpResponseRedirect(reverse('main:index'))  # Функция reverse преобразует 'main:index' в url и перенаправляет 
    else:
        form = UserRegistrationForm()  

    context = {
        'title': 'Home - registration',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile was updated successfully")
                return HttpResponseRedirect(reverse('users:profile'))  # Функция reverse преобразует 'main:index' в url и перенаправляет 
    else:
        form = UserRegistrationForm(instance=request.user) 

    context = {
        'title': 'Home - profile',
        'form': form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, successfully logout")
    auth.logout(request)
    return redirect(reverse('main:index'))