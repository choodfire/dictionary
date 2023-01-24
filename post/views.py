from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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
        comment.post = self.object
        comment.save()

        return redirect(reverse('post:post', kwargs={'pk': self.object.id}))


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
    template_name = 'post/createPost.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('post:post', kwargs={'pk': self.object.id})


class EditPost(TitleMixin, UpdateView):
    model = Post
    title = "Edit post"
    fields = ['title', 'description', 'text', 'image']
    template_name = 'post/editPost.html'

    def get_success_url(self):
        # return reverse_lazy('post:post', args = (self.object.id,))
        return reverse('post:post', kwargs={'pk': self.object.id})


class DeletePost(LoginRequiredMixin, TitleMixin, DeleteView):
    model = Post
    title = "Delete post"
    login_url = '/login/'
    template_name = 'post/deletePost.html'

    def get_success_url(self):
        return reverse('user:profile')
