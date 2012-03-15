# Create your views here.
from MyWorldUsers.models import UserProfile
from Places.models import CommentRating, Place
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext


def add_comment_rating(request):
#    request_username = request.GET["username"]
#    request_place_titile = request.GET["place_title"]
#    request_description = request.GET["description"]
#    request_longitude = request.GET["longitude"]
#    request_latitude = request.GET["latitude"]
#    request_comment = request.GET["comment"]
#    request_rating = request.GET["rating"]
#    request_posted_on = DateTime.today().now()
    #if place_title exists with same longitude and latitude
    #add the comments and ratings to comment table
    #else if place_title exists but with different longitude and latitude add place and then comments and ratings
    #add the place to Place table then add comments and ratings
    pass


def places_near_by(request):
    request_longitude = request.POST["longitude"]
    request_latitude = request.POST["latitude"]
    #retrieve near by places using filter gte lte
    pass


def all_places(request):
    request_longitude = request.POST["longitude"]
    request_latitude = request.POST["latitude"]
    pass


@login_required
def view_comments(request):
    #import pdb
    #pdb.set_trace()
    user_profile_object = UserProfile.objects.get(id=request.session.get('user_id'))
    comments_ratings_object = CommentRating.objects.filter(user=user_profile_object)
    data = {"user_profile_object": user_profile_object, "comments_ratings_object": comments_ratings_object}
    return render_to_response("view_comments.html", data, context_instance=RequestContext(request))


