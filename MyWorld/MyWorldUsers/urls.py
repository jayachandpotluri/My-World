from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('MyWorld.MyWorldUsers.views',
    url(r'user_authentication/', 'user_authentication', name='user_authentication'),
    url(r'register_user/', 'register_user', name='register_user'),
    url(r'change_password/', 'change_password', name='change_password'),
)