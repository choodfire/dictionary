from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainPage')
    else:
        form = RegistrationForm()

    context = {
        "form": form
    }

    return render(request, 'registration/sign_up.html', context)