from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post
from django.urls import reverse
from .forms import PostForm
from calendar import month_name
from comment.models import Comment
from comment.forms import CommentForm

def post(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentCreator = request.user
            comment.post = Post.objects.get(id=id)
            comment.save()

            return redirect(reverse('post', kwargs={ 'id': id }))

    template = loader.get_template('post/post.html')

    post = Post.objects.get(id=id)
    postsSeeAlso = Post.objects.filter(featured=False).order_by('-id')[:3]
    comments = Comment.objects.filter(post=post).order_by('-id')
    form = CommentForm()

    context = {
        "post": post,
        "Title": post.title,
        "postsSeeAlso": postsSeeAlso,
        "comments": comments,
        "form": form
    }

    return HttpResponse(template.render(context, request))

def search(request):
    searchString = request.GET["search"]
    template = loader.get_template('post/searchResults.html')

    posts = Post.objects.filter(title__icontains=searchString)
    searchTitle = f"Found by \"{searchString}\""
    context = {
        "posts": posts,
        "Title": "Search",
        "searchString": searchTitle
    }

    return HttpResponse(template.render(context, request))


def searchByDate(request, year, month):
    template = loader.get_template('post/searchResults.html')

    posts = Post.objects.filter(releaseDate__year=year, releaseDate__month=month)
    monthString = month_name[month]
    searchString = f"Posts from {monthString} {year}"
    context = {
        "posts": posts,
        "Title": "Search",
        "searchString": searchString
    }

    return HttpResponse(template.render(context, request))

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
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        "post": post,
        "Title": "Edit post",
        "form": form,
    }

    return render(request, 'post/editPost.html', context)


def deletePost(request, id):
    postToDelete = Post.objects.get(id=id)
    postToDelete.delete()

    return HttpResponseRedirect(reverse('profile'))


