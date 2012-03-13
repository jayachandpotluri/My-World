from django.db import models
from MyWorld.MyWorldUsers.models import UserProfile
# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=75)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    posted_by = models.ForeignKey(UserProfile)
    posted_on = models.DateTimeField()
    
    def __unicode__(self):
        return "Title: " + self.title

rating_choices = (
    (1, 'Very Poor'),
    (2, 'Poor'),
    (3, 'Average'),
    (4, 'Good'),
    (5, 'Very Good')
)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    place = models.ForeignKey(Place)
    comment = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    
    def __unicode__(self):
        return "Place: %s Rating: %s" % (self.place.title, rating_choices[str(self.rating)])
    