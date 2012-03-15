"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from MyWorldUsers.models import UserProfile
import json


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    
    def test_add_comment_rating(self):
        client_object = Client()
        response = client_object.post('/register_user/', {'name': 'jay', 'email': 'jayachand.potluri@mutualmobile.com', 'udid': '1234'})
        self.assertContains(response, text='User Registration Successfull')
        response = client_object.post('/add_comment_rating/', {'': '', '': '', '': '', '': ''})
        self.assertContains(response, text='Comment Added Successfully')
