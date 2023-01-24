from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, TemplateView, MonthArchiveView, \
    ListView
from django.views.generic.edit import FormMixin

from .models import Post
from django.urls import reverse
from .forms import PostForm
from calendar import month_name
from comment.models import Comment
from comment.forms import CommentForm

class PostView(DetailView, FormMixin):
    template_name = 'post/post.html'
    queryset = Post.objects.all()
    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['Title'] = post.title
        context['postsSeeAlso'] = Post.objects.filter(featured=False).exclude(id=post.id)[:3]
        context['comments'] = Comment.objects.filter(post=post)
        context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        comment = form.save(commit=False)
        comment.commentCreator = self.request.user
        comment.post = self.get_object()
        comment.save()

        return redirect(reverse('post', kwargs={ 'pk': self.get_object().id }))


# def search(request):
#     searchString = request.GET["search"]
#     template = loader.get_template('post/searchResults.html')
#
#     posts = Post.objects.filter(title__icontains=searchString)
#     searchTitle = f"Found by \"{searchString}\""
#     context = {
#         "posts": posts,
#         "Title": "Search",
#         "searchString": searchTitle
#     }
#
#     return HttpResponse(template.render(context, request))

class Search(ListView):
    model = Post
    template_name = 'post/searchResults.html'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET['search'])

class SearchByDate(MonthArchiveView):
    template_name = 'post/searchResults.html'
    queryset = Post.objects.all()
    date_field = "releaseDate"
    allow_future = False
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = "Search"
        context['searchString'] = f"Posts from {month_name[self.get_month()]} {self.get_year()}"
        return context


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