from django.test import TestCase, Client
from django.urls import reverse
from main.models import Url


class TestViews(TestCase):
    """Create a new Url, after that, compare with response"""
    def setUp(self):
        """getting"""
        self.url1 = Url.objects.create(
        	title = "Google",
        	reference = "https://www.google.com.ua/", 
        	)

    def test_requests_view(self):
        """compare"""
        client = Client()
        print()
        response = client.get(reverse('home'))
        self.assertTemplateUsed(response, 'main/main.html')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.url1.title)
        self.assertContains(response, self.url1.reference)
