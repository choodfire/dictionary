from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView

from post.models import Post
# Create your views here.

class MainPage(TemplateView):
    template_name = 'core/mainPage.html'

    def get_title(self):
        return "Blogs"

    def get_featured_posts(self):
        return Post.objects.filter(featured=True)

    def get_non_featured_posts(self):
        return Post.objects.filter(featured=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = self.get_title()
        context['posts'] = self.get_non_featured_posts()
        context['featuredPosts'] = self.get_featured_posts()
        return context

class About(TemplateView):
    template_name = 'core/about.html'

    def get_title(self):
        return "About"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = self.get_title()

        return context