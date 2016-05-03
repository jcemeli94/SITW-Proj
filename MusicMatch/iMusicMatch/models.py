from django.db import models

#Group, users, playlists, tracks

from django.contrib.auth.models import User as Django_User, Group

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(Django_User)

    # The additional attributes we wish to include.
    realName = models.CharField(max_length=100)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class User(models.Model):
    scID = models.IntegerField()
    permalink = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # userPlaylists = models.ManyToManyField(Playlist)
    # userTracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class Track(models.Model):
    scID = models.IntegerField()
    name = models.CharField(max_length=100)
    duration = models.IntegerField() #Time in seconds
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class Group(models.Model):
    scID = models.IntegerField() #ID used in SoundCloud API
    name = models.CharField(max_length=100)
    userList = models.ManyToManyField(User)
    tracks = models.ManyToManyField(Track, blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class Playlist(models.Model):
    scID = models.IntegerField()
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    trackList = models.ManyToManyField(Track)

    def __unicode__(self):
        return "{0}, {1}".format(self.scID, self.name)

class PlaylistReview(models.Model):
    playlistID = models.ForeignKey(Playlist)
    user = models.ForeignKey(Django_User)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.id, self.playlistID.name, self.user.username)

class GroupReview(models.Model):
    groupID = models.ForeignKey(Group)
    user = models.ForeignKey(Django_User)
    date = models.DateField()
    review = models.CharField(max_length = 1000)

    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.id, self.groupID.name, self.user.username)