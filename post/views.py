from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import DeleteView, UpdateView, CreateView

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
    postsSeeAlso = Post.objects.filter(featured=False).exclude(id=post.id)[:3]
    comments = Comment.objects.filter(post=post)
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


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'description', 'text', 'image']


class EditPost(UpdateView): # todo titlemixin
    model = Post
    fields = ['title', 'description', 'text', 'image']
    template_name_suffix = '_update_form'


class DeletePost(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('mainPage')