from django.db import models

#Group, users, playlists, tracks

from django.contrib.auth.models import User

class Group(models.Group):
    scID = models.IntegerField() #ID used in SoundCloud API
    name = models.CharField()
    userList = models.ManytoManyField(User)

    def __unicode__(self):
        return self.scID+" - "+self.name

class User(models.User):
    scID = models.IntegerField()
    name = models.CharField()
    userPlaylists = models.ManytoManyField(Playlist)
    userTracks = models.ManytoManyField(Track)

    def __unicode__(self):
        return self.scID+" - "+self.name

class Playlist(models.Playlist):
    scID = models.IntegerField()
    name = models.CharField()
    ownUsers = models.ManytoManyField(User)
    trackList = models.ManytoManyField(Track)

    def __unicode__(self):
        return self.scID+" - "+self.name

class Track(models.Playlist):
    scID = models.IntegerField()
    name = models.CharField()
    duration = models.IntegerField() #Time in seconds
    ownUsers = models.ManytoManyField(User)
    isInPlaylist = models.ManytoManyField(Playlist)

    def __unicode__(self):
        return self.scID+" - "+self.name

class PlaylistReview(model.PlaylistReview):
    scID = models.IntegerField() #Playlist ID in SoundCloud
    username = models.CharField(max_length = 20)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.scID+" - "+self.username+" - "+self.date

class GroupReview(model.PlaylistReview):
    scID = models.IntegerField() #Group ID in SoundCloud
    username = models.CharField(max_length = 20)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.scID+" - "+self.username+" - "+self.date