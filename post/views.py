from django.shortcuts import redirect
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, MonthArchiveView, ListView
from django.views.generic.edit import FormMixin
from .models import Post
from django.urls import reverse
from calendar import month_name
from comment.models import Comment
from comment.forms import CommentForm
from views.mixins import TitleMixin


class PostView(FormMixin, TitleMixin, DetailView):
    template_name = 'post/post.html'
    queryset = Post.objects.all()
    form_class = CommentForm

    def get_title(self):
        return self.object.title

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
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

        return redirect(reverse('post', kwargs={'pk': self.get_object().id}))


class Search(TitleMixin, ListView):
    model = Post
    template_name = 'post/searchResults.html'
    title = "Search"

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET['search'])


class SearchByDate(TitleMixin, MonthArchiveView):
    template_name = 'post/searchResults.html'
    queryset = Post.objects.all()
    date_field = "releaseDate"
    allow_future = False
    allow_empty = True
    title = "Search"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchString'] = f"Posts from {month_name[self.get_month()]} {self.get_year()}"
        return context


class CreatePost(TitleMixin, CreateView):
    model = Post
    title = "Create post"
    fields = ['title', 'description', 'text', 'image']


class EditPost(TitleMixin, UpdateView):
    model = Post
    title = "Edit post"
    fields = ['title', 'description', 'text', 'image']
    template_name_suffix = '_update_form'


class DeletePost(TitleMixin, DeleteView):
    model = Post
    title = "Delete post"

    def get_success_url(self):
        return reverse('mainPage')
