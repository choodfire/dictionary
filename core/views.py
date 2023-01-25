from django.views.generic import TemplateView
from views.mixins import TitleMixin
from post.models import Post
from django.db.models import Count


class MainPage(TitleMixin, TemplateView):
    template_name = 'core/mainPage.html'
    title = "Articles"

    # def get_posts(self, sort_type):
    #     posts = None
    #
    #     match sort_type:
    #         case "by_popularity":
    #             posts = Post.objects.filter(featured=False).annotate(num_comments=Count('comment')).order_by(
    #                 '-num_comments')
    #         case "by_name":
    #             posts = Post.objects.filter(featured=False).order_by('title')
    #         case "by_date" | _:  # default - by release date
    #             posts = Post.objects.filter(featured=False)
    #
    #     return posts

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(featured=False)
        context['featuredPosts'] = Post.objects.filter(featured=True)
        return context


class About(TitleMixin, TemplateView):
    template_name = 'core/about.html'
    title = "About"
