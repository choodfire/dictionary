from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    text = models.TextField(max_length=20000)
    image = models.ImageField(upload_to="images")
    releaseDate = models.DateTimeField(null=False, blank=False, default=django.utils.timezone.now)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = "Post"
        verbose_name_plural = "Posts"