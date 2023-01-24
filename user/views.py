from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
from .forms import RegistrationForm
from django.contrib.auth import login
from post.models import Post
from django.http import HttpResponseRedirect
from views.mixins import TitleMixin


class SignUp(TitleMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    title = "Sign up"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_successful_url())

    def get_successful_url(self):
        return reverse('core:mainPage')

class Profile(LoginRequiredMixin, TitleMixin, TemplateView):
    model = Post
    template_name = "user/profile.html"
    login_url = '/login/'

    def get_title(self):
        return self.request.user.username

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(creator=self.request.user)

        return context

class Logout(LogoutView):
    def get_success_url(self):
        return reverse('core:mainPage')

class Login(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('core:mainPage')
