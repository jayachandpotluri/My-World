from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class UserProfileManager(models.Manager):
#    def generate_username_password(self, email):
#        pass


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    udid = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "User: " + unicode(self.user.username)