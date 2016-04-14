from django.db import models

#Group, users, playlists, tracks

from django.contrib.auth.models import User
from django.contrib.auth.models import *

class Group(models.Model):
    scID = models.IntegerField() #ID used in SoundCloud API
    name = models.CharField(max_length=100)
    userList = models.ManyToManyField(User)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class Track(models.Model):
    scID = models.IntegerField()
    name = models.CharField(max_length=100)
    duration = models.IntegerField() #Time in seconds
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class Playlist(models.Model):
    scID = models.IntegerField()
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    trackList = models.ManyToManyField(Track)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class User(models.Model):
    scID = models.IntegerField()
    name = models.CharField(max_length=100)
    userPlaylists = models.ManyToManyField(Playlist)
    userTracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class PlaylistReview(models.Model):
    scID = models.IntegerField() #Playlist ID in SoundCloud
    username = models.CharField(max_length = 20)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.username)

class GroupReview(models.Model):
    scID = models.IntegerField() #Group ID in SoundCloud
    username = models.CharField(max_length = 20)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.username)