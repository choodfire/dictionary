from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from post.models import Post
# Create your views here.

def mainPage(request):
    template = loader.get_template('core/mainPage.html')

    featuredPosts = Post.objects.filter(featured=True)
    posts = Post.objects.filter(featured=False).order_by('-id')
    context = {
        "posts": posts,
        'featuredPosts': featuredPosts,
        "Title": "Blogs"
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('core/about.html')

    return HttpResponse(template.render({}, request))