from django.views.generic import TemplateView
from views.mixins import TitleMixin
from post.models import Post

class MainPage(TitleMixin, TemplateView): # todo mb listview
    template_name = 'core/mainPage.html'
    title = "Articles"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(featured=False)
        context['featuredPosts'] = Post.objects.filter(featured=True)
        return context


class About(TitleMixin, TemplateView):
    template_name = 'core/about.html'
    title = "About"