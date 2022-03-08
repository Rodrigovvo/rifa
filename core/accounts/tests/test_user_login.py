import json

from django.apps.registry import Apps
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


User = get_user_model()
client = Client()


class TestUserLogin(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    
    def test_if_password_incorrect_then_cant_login(self):
        # unit test
        # Corroborate that user's password needs to be only the correct one
        pass
    
    def test_if_user_not_registered_cant_login(self):
        # unit test
        # Corroborate that user's are able to login only if they're registered
        pass