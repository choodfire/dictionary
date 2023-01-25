import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.Filter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('title', )