# Create your views here.
from MyWorldUsers.models import UserProfile
from MyWorldUsers.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import json, string, random


class JSONResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super(JSONResponse, self).__init__(args, kwargs)
        self.status_code = 200
        self['Content-Type'] = 'application/json'


@csrf_exempt
def user_authentication(request):
    #import pdb
    #pdb.set_trace()
    if request.method == "POST":
        #post_data = request.raw_post_data
        #request_username = post_data("1")
        #request_password = post_data("2")
        request_username = request.POST.get("username")
        request_password = request.POST.get("password")
    elif request.method == "GET":
        request_username = request.GET.get("username")
        request_password = request.GET.get("password")
        #status = "not in post"
        #return HttpResponse(json.dumps(status), mimetype="application/json")
    try: 
        user = authenticate(username=request_username, password=request_password)
        if user is not None:
            status = "User Authentication successfull"
        else:
            status = "User Authentication failed"
    except:
        status = "User Authentication failed"
    return HttpResponse(json.dumps(status), mimetype="application/json")
    #return JSONResponse(simplejson.dumps(status))


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        request_email = request.POST.get("email")
        request_name = request.POST.get("name")
        request_username = request_email
        request_udid = request.POST.get("udid")
    if request.method == "GET":
        request_email = request.GET.get("email")
        request_name = request.GET.get("name")
        request_username = request_email
        request_udid = request.GET.get("udid")
    #import pdb
    #pdb.set_trace()
    try:
        User.objects.get(email=request_email)
        status = "User already exists"
    except:
        user_object = User(username=request_username, first_name=request_name, email=request_email)
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
        status = "User Registration Successfull"
    return HttpResponse(json.dumps(status), mimetype="application/json")
    #return JSONResponse(simplejson.dumps(status))


def change_password(request):
    request_username = request.POST["username"]
    request_old_password = request.POST["old_password"]
    request_new_password = request.POST["new_password"]
    user = authenticate(username=request_username, password=request_old_password)
    if user is not None:
        status = "User Authentication successfull"
    else:
        status = "User Authentication failed"
    try:
        user_object = User.objects.get(username=request_username)
        user_object.set_password(request_new_password)
        user_object.save()
        status = "Password changed successfully"
    except:
        status = "Password change unsuccessfull"
    return HttpResponse(json.dumps(status), mimetype="application/json")


def home_page(request):
    return render_to_response("home.html", {}, context_instance=RequestContext(request))


def login_form(request):
    user_authentication = True
    if request.method == "GET":
        form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            request_username = request.POST["username"]
            request_password = request.POST["password"]
            user_object = authenticate(username=request_username, password=request_password)
            if user_object:
                login(request, user_object)
                user_profile_object = UserProfile.objects.get(user=user_object)
                request.session['user_id'] = user_profile_object.id
                #return render_to_response("view_comments.html", data, context_instance=RequestContext(request))
                return HttpResponseRedirect(reverse('view_comments'))
            else:
                user_authentication = False
    data = {'form': form, 'user_authentication': user_authentication}
    return render_to_response("home.html", data, context_instance=RequestContext(request))