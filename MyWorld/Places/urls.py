from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('MyWorld.Places.views',
    #url(r'add_comment_rating', 'add_comment_rating', name='add_comment_rating')
    url(r'view_comments', 'view_comments', name='view_comments'),
)