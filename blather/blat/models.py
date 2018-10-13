""" model for blat """
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blat(models.Model):
    """ Blat model to store blats """
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def total_likes(self):
        """ get total likes count for each Blat """
        return self.like_set.count()

    def __str__(self):
        """ to get the string rep of the blats """
        return self.text[:50]


class Like(models.Model):
    """ holds the like info of each blat """
    blat = models.ForeignKey(Blat, on_delete=models.CASCADE)

class Profile(models.Model):
    """ Profile model to extend Users model provided by django """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    blog = models.URLField(blank=True)
