from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
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
        return reverse('mainPage')


class Profile(TitleMixin, TemplateView):
    model = Post
    template_name = "user/profile.html"

    def get_title(self):
        return self.request.user.username

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(creator=self.request.user)

        return context