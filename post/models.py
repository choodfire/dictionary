from django.db import models
import django.utils.timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=False, blank=False, max_length=255)
    text = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False, upload_to="images")
    releaseDate = models.DateTimeField(null=False, blank=False, default=django.utils.timezone.now())
    featured = models.BooleanField(default=False)