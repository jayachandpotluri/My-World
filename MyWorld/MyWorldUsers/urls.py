from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('MyWorld.MyWorldUsers.views',
    url(r'user/authentication', 'user_authentication', name='user_authentication'),
    url(r'register/user', 'register_user', name='register_user'),
    url(r'change/password', 'change_password', name='change_password'),
    url(r'login/', 'login_form', name='login_form'),
)