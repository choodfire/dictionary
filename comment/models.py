from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from post.models import Post


class Comment(models.Model):
    commentCreator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentCreator')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=django.utils.timezone.now)
    text = models.TextField(max_length=500)

    class Meta:
        ordering = ['-id']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
