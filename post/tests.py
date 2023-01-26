from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .models import Post
from django.contrib.auth.models import User
from post.filters import PostFilter
from django.test.client import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile


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


class Response200Test(TestCase):
    def setUp(self):
        self.client = Client()
        Post.objects.create(title=f"Post1",
                            description="Test descr",
                            text="Test text",
                            image=SimpleUploadedFile(name='test_image.jpg', content=open('/home/ruslan/Pictures/Screenshots/Screenshot from 2023-01-17 17-36-04.png', 'rb').read(), content_type='image/jpeg'))

    def testWithoutParams(self):
        response = self.client.get('post:post')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/results/', args={})
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/results/{datetime.now().year}/{datetime.now().month}/', args={})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/login/', {'username': 'qq', 'password': 'zxccxz88'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('post:createPost'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/edit/1/', args={})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/delete/1/', args={})
        self.assertEqual(response.status_code, 302) # redirect

    def testWithParams(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/results/', args={'title': 'post'})
        self.assertEqual(response.status_code, 200)
