from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from post.filters import PostFilter
from django.test.client import RequestFactory


class ClassStr(TestCase):
    def setUp(self):
        self.post = Post(creator=User(),
                         title="Django article",
                         description="Short article about Django framework",
                         text="""Django is a free and open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit. Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.""",
                         image=None)

    def testStr(self):
        self.assertEqual(str(self.post), "Django article")

class FilterTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        qset = None
        for i in range(1, 11):
            if i % 2 == 0:
                Post.objects.create(title=f"Odd{i}",
                                    description="Test descr",
                                    text="Test text")
            else:
                Post.objects.create(title=f"Even{i}",
                                    description="Test descr",
                                    text="Test text")

    def testFilter(self):
        request = self.factory.get('/results/?title=Odd')
        filterRes = PostFilter(request.GET).qs

        rightRes = Post.objects.filter(title__icontains="Odd")

        self.assertEqual(list(filterRes), list(rightRes)) # list because queryset object has many attributes that useless but may be different
