from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from .urls import *

# Create your tests here.

class Response200Test(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='qq')
        user.set_password('zxccxz88')
        user.save()

    def testWithoutParams(self):
        response = self.client.get(reverse('profile:login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('profile:profile'))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('profile:signup'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('profile:logout'))
        self.assertEqual(response.status_code, 302) #  redirect to login



    def testWithParams(self):
        self.client.login(username='qq', password='zxccxz88')

        self.assertEqual(auth.get_user(self.client).is_authenticated, True)

        response = self.client.get(reverse('profile:profile'))
        self.assertEqual(response.status_code, 200)
