from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from post.models import Post
from django.http import HttpResponse
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
        "form": form,
        "Title": "Sign up"
    }

    return render(request, 'registration/sign_up.html', context)

def profile(request):
    template = loader.get_template('user/profile.html')

    posts = Post.objects.filter(creator=request.user)

    title = f"Profile {request.user.username}"

    context = {
        "posts": posts,
        "Title": title
    }

    return HttpResponse(template.render(context, request))