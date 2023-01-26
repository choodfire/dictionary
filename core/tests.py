from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class Response200Test(TestCase):
    def setUp(self):
        pass

    def testWithoutParams(self):
        response = self.client.get(reverse('core:mainPage'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)

