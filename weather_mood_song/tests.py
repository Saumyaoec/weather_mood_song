from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserInput

class UserInputModelTest(TestCase):
    def setUp(self):
        self.user_input = UserInput.objects.create(mood='Happy', city='London')

    def test_user_input_model(self):
        self.assertEqual(self.user_input.mood, 'Happy')
        self.assertEqual(self.user_input.city, 'London')

class APIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_input_mood_post(self):
        url = reverse('input_mood')
        data = {'mood': 'Happy', 'city': 'London'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_match_weather_with_mood_get(self):
        url = reverse('match_weather_with_mood')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
