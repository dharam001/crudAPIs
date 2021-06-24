from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User

from model_bakery import baker


class UserListRoutesTests(APITestCase):
    # Test user list url
    def test_url_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class UserCreateTests(APITestCase):
    # Test create user api with valid data
    def test_user_create_route_with_valid_data_returns_201(self):
        url = reverse('create-user')
        data = {
            "username": "JohnK",
            "first_name": "John",
            "last_name": "K",
            "email": "john@gmail.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().first_name, 'John')


class UserDetailRoutesTests(APITestCase):
    # Test url for user-detail route
    def test_url_to_get_details_of_individual_user(self):
        user = baker.make('User')
        url = reverse('user-details', args=[user.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserUpdateRouteTests(APITestCase):
    # Test update user with valid data should return HTTP status 200
    def test_user_update_route_with_valid_data_returns_200(self):
        user = baker.make('User')
        url = reverse('update-user', args=[user.pk])
        data = {
            "username": "John",
            "first_name": "Johny",
            "last_name": "K",
            "email": "john@gmail.com"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().first_name, 'Johny')


class UserDeleteRouteTests(APITestCase):

    # Test route for delete user
    def test_user_delete_route(self):
        user = baker.make('User')
        url = reverse('delete-user', args=[user.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test delete user uel with valid data should return HTTP no content status
    def test_user_delete_route_with_valid_data_returns_204(self):
        user = baker.make('User')
        url = reverse('delete-user', args=[user.pk])
        data = {
            "username": "John",
            "first_name": "Johny",
            "last_name": "K",
            "email": "john@gmail.com"
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
