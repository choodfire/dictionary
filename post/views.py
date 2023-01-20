from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post
from django.urls import reverse
from .forms import PostForm

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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()

            return redirect('mainPage')
    else:
        form = PostForm()

    context = {
        "form": form,
        "Title": "Create post"
    }

    return render(request, 'post/createPost.html', context)

def editPost(request, id):
    if request.method == "POST":
        currentPost = Post.objects.get(id=id)
        currentPost = Post(title=request.POST["title"],
                           description=request.POST["description"],
                           text=request.POST["text"],
                           image=request.POST["image"])
        currentPost.save()
        return redirect('mainPage')
    else:
        post = Post.objects.get(id=id)
        context = {
            "post": post,
            "Title": "Edit post"
        }

        return render(request, 'post/updatePost.html', context)


def deletePost(request, id):
    postToDelete = Post.objects.get(id=id)
    postToDelete.delete()

    return HttpResponseRedirect(reverse('profile'))


