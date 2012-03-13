# Create your views here.
from MyWorld.MyWorldUsers.models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
import json, string, random
from django.core.mail import EmailMessage

def user_authentication(request):
    request_username = request.POST["username"]
    request_password = request.POST["password"]
    status = False
    user = authenticate(username=request_username, password=request_password)
    if user is not None:
        status = True
    return HttpResponse(json.dumps(status), mimetype="application/json")

def register_user(request):
    status = "False"
    request_email = request.GET["email"]
    request_first_name = request.GET["first_name"]
    request_username = request_email
    request_udid = request.GET["udid"]
    try:
        user_test = User.objects.get(email=request_email)
        status = "User already exists"
    except:
        user_object = User(username=request_username, first_name=request_first_name, email=request_email)
        #generating the password
        all_characters = string.digits + string.letters + "~!@#$%^&*()_+"
        generated_user_password = "".join([random.choice(all_characters) for el in range(8)])
        
        user_object.set_password(generated_user_password)
        user_object.save()
        user_profile_object = UserProfile(user=user_object, udid=request_udid)
        user_profile_object.save()
        #sending the email
        ip_address = "http://127.0.0.1:8000/login"
        body_message = """Thank you for registerting at My World.
        \nThe credentials are:\n username: %s\npassword: %s\n Use %s to login""" % (request_email, generated_user_password, ip_address) 
        email = EmailMessage(subject='Registration Successfull at My World', body=body_message, to=[request_email])
        email.send()
        
        status = "Successfully added"
    return HttpResponse(json.dumps(status), mimetype="application/json")


def change_password(request):
    pass