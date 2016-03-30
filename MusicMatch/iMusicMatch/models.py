from django.db import models

#Group, users, playlists, tracks

from django.contrib.auth.models import User

class Group(models.Group):
    scID = models.IntegerField() #ID used in SoundCloud API
    userList = models.ManytoManyField(User)

class User(models.User):
    scID = models.IntegerField()
    userPlaylists = models.ManytoManyField(Playlist)
    userTracks = models.ManytoManyField(Track)

class Playlist(models.Playlist):
    scID = models.IntegerField()
    ownUsers = models.ManytoManyField(User)
    trackList = models.ManytoManyField(Track)

class Track(models.Playlist):
    scID = models.IntegerField()
    duration = models.IntegerField() #Time in seconds
    ownUsers = models.ManytoManyField(User)
    isInPlaylist = models.ManytoManyField(Playlist)
