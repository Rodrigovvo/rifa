import json

from django.apps.registry import Apps
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from api import views


User = get_user_model()
client = Client()
factory = APIRequestFactory()

class TestUserLogin(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
        }
        self.test_user = User.objects.create_user(**self.credentials)

    def test_create_user(self):
        logged = self.client.login(**self.credentials)
        data = {
            'username': 'testuser2',
            'password': 'test',

        }
        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_same_username(self):
        logged = self.client.login(**self.credentials)
        data = {
            'username': 'testuser',
            'password': 'test',

        }
        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_by_unlogged_user(self):
        data = {
            'username': 'testuser2',
            'password': 'test',

        }
        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user(self):
        logged = self.client.login(**self.credentials)
        data = {
            'username': 'testuser2',
            'password': 'test',

        }

        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data['username'], data['username'])
        user_for_delete = User.objects.get(username=data['username'])
        response = self.client.delete(f'/api/v1/users/{user_for_delete.pk}/')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_user_with_patch(self):
        logged = self.client.login(**self.credentials)
        response = self.client.patch(f'/api/v1/users/{self.test_user.pk}/', {'email' : 'email@email.com'})
        self.assertFalse(self.test_user.email, 'email@email.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_with_put(self):
        logged = self.client.login(**self.credentials)
        self.credentials['email'] ='email@email.com'
        response = self.client.put(f'/api/v1/users/{self.test_user.pk}/', self.credentials)
        self.assertFalse(self.test_user.email, 'email@email.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
