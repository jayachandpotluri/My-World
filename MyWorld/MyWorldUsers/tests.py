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
    
    def test_user_authentication(self):
        """
        Tests the user authentication
        """
        client_object = Client()
        response = client_object.post('/user/authentication/', {'username': 'jay', 'password': 'admin'})
        #self.assertContains(response, text='User Authentication successfull')
        self.assertEqual(200, response.status_code)
    
    def test_register_user(self):
        """
        Tests the user registration
        """
        client_object = Client()
        #Test for successfull registration
        response = client_object.post('/register/user/', {'name': 'jay', 'email': 'jayachand.potluri@mutualmobile.com', 'udid': '1234'})
        self.assertContains(response, text='User Registration Successfull')
        user_count_before_adding = User.objects.all().count()
        response = client_object.post('/register/user/', {'name': 'uday', 'email': 'uday12kumar@gmail.com', 'udid': '1234'})
        self.assertContains(response, text='User Registration Successfull')
        user_count_after_adding = User.objects.all().count()
        #Test for user existance
        self.assertEqual(user_count_before_adding+1, user_count_after_adding)
        response = client_object.post('/register/user/', {'name': 'jay', 'email': 'jayachand.potluri@mutualmobile.com', 'udid': '1234'})
        self.assertContains(response, text='User already exists')
    
    def test_change_password(self):
        """
        Tests the change of password. This method is called for the first time when the user logs in
        """
        client_object = Client()
        response = client_object.post('/register/user/', {'name': 'jay', 'email': 'jayachand.potluri@mutualmobile.com', 'udid': '1234'})
        self.assertContains(response, text='User Registration Successfull')
        response = client_object.post("/change/password/", {'username': 'jayachand.potluri@mutualmobile.com', 'old_password': 'admin', 'new_password': 'admin'})
        self.assertContains(response, text='Password changed successfully')
    
    def test_home_page(self):
        client_object = Client()
        response = client_object.post('/home/page/')
        self.assertEquals(response.status_code, 200)

    def test_login_form(self):
        client_object = Client()
        response = client_object.post('/login/form/', {'username': 'jay', 'password': 'admin'})
        self.assertEquals(response.status_code, 200)
    