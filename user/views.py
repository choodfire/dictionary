from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from post.models import Post
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class SignUp(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'

    def get_title(self):
        return "Sign up"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = self.get_title()
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_successful_url())

    def get_successful_url(self):
        return reverse('mainPage')


class Profile(TemplateView):
    model = Post
    template_name = "user/profile.html"

    def get_posts(self):
        return Post.objects.filter(creator=self.request.user)

    def get_title(self):
        return f"Profile {self.request.user.username}"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        context['posts'] = self.get_posts()

        return context