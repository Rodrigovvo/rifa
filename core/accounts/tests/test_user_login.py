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
            'password': 'secret',
            }
        user = User.objects.create_user(**self.credentials)


    def test_login(self):
        logged = self.client.login(**self.credentials)
        self.assertTrue(logged)


    def test_login_HTTP_response(self):
        response = self.client.post('/api-auth/login/',**self.credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_if_password_incorrect_then_cant_login(self):
        self.credentials['password'] = 'wrong_password'
        logged = self.client.login(**self.credentials)
        self.assertFalse(logged)


    def test_if_password_incorrect_then_cant_login_HTTP_response(self):
        self.credentials['password'] = 'wrong_password'
        response = self.client.post('/api-auth/login/',**self.credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_if_user_not_registered_cant_login(self):
        unregistered_user = {
            'username': 'unregistered_user',
            'password': 'secr3t',
        }
        logged = self.client.login(**unregistered_user)
        self.assertFalse(logged)


    def test_if_user_not_registered_cant_login_HTTP_response(self):
        unregistered_user = {
            'username': 'unregistered_user',
            'password': 'secr3t',
        }
        response = self.client.post('/api-auth/login/', **unregistered_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
