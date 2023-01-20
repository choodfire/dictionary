from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post
from django.urls import reverse
from .forms import AddPostForm

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

def createPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            newPost = Post(title=data['title'], description=data['description'], text=data['text'], image=data['image'], creator=request.user)
            newPost.save()
            return redirect('mainPage')
            # todo make through modelform
    else:
        form = AddPostForm()

    context = {
        "form": form,
        "Title": "Create post"
    }

    return render(request, 'post/createPost.html', context)

def editPost(request, id):
    pass

def deletePost(request, id):
    postToDelete = Post.objects.get(id=id)
    postToDelete.delete()

    return HttpResponseRedirect(reverse('profile'))


