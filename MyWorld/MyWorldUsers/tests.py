"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from MyWorld.MyWorldUsers.models import UserProfile

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
        client_check = Client()
        response = client_check.post('/user_authentication/', {'username': 'jay', 'password': 'admin'})
        self.assertEqual(200, response.status_code)
    
    def test_register_user(self):
        """
        Tests the user registration
        """
        client_check = Client()
        user_count_before_post = UserProfile.objects.all().count()
        response = client_check.post('/register_user/', {'first_name': 'jay', 'email': 'jayachand.potluri@mutualmobile.com', 'udid': '1234'})
        user_count_after_post = UserProfile.objects.all().count()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(user_count_before_post+1, user_count_after_post)
    
    #def test_change_password(self):
    #    """
    #    Tests the change of password. This method is called for the first time when the user logs in
    #    """
    #    client_check = Client()
    #    response = client_check_post("/change_password/", {'username': '', 'pasword': ''})
    #    self.assertEqual(200, response.status_code)
    