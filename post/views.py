from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Post
from django.urls import reverse
from .models import Post

# Create your views here.
def mainPage(request):
    template = loader.get_template('post/mainPage.html')

    featuredPosts = Post.objects.filter(featured=True)
    posts = Post.objects.filter(featured=False)
    context = {
        "posts": posts,
        'featuredPosts': featuredPosts,
        "Title": "Blogs"
    }

    return HttpResponse(template.render(context, request))

def post(request, id):
    template = loader.get_template('post/post.html')

    post = Post.objects.get(id=id)
    postsSeeAlso = Post.objects.filter(featured=False).order_by('-id')[:3]

    context = {
        "post": post,
        "Title": post.title,
        "postsSeeAlso": postsSeeAlso
    }

    return HttpResponse(template.render(context, request))

def search(request):
    searchString = request.GET["search"]
    template = loader.get_template('post/searchResults.html')

    posts = Post.objects.filter(title__icontains=searchString)

    context = {
        "posts": posts,
        "Title": "Search"
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('post/about.html')

    return HttpResponse(template.render({}, request))

def create(request):
    template = loader.get_template('post/createPost.html')
    return HttpResponse(template.render({"Title": "Add post"}, request))

def createResult(request):
    titleReceived = request.POST["title"]
    descriptionReceived = request.POST["description"]
    textReceived = request.POST["text"]
    imageReceived = request.POST["image"]
    newPost = Post(title=titleReceived, description=descriptionReceived, text=textReceived, image=imageReceived)

    newPost.save()

    return HttpResponseRedirect(reverse('mainPage'))

