import collections
from rest_framework import serializers
from django.contrib.auth.models import User as Django_User
from iMusicMatch.models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    scID = serializers.IntegerField()  # ID used in SoundCloud API
    name = serializers.CharField(max_length=100)
    userList = serializers.SerializerMethodField('get_userlist')
    tracks = serializers.SerializerMethodField('get_tracks')


    def get_userlist(self, group):
        userlist = []
        for user in User.objects.filter(group=group).order_by('id'):
            userlist.append("http://127.0.0.1:8000/api/users/" + str(user.id))
        return userlist
    class Meta:
        model = Group

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    scID = serializers.IntegerField()  # ID used in SoundCloud API
    name = serializers.CharField(max_length=100)
    members = serializers.SerializerMethodField('get_userlist')
    trackList = serializers.SerializerMethodField('get_tracklist')

    def get_userlist(self, group):
        userlist = []
        for user in User.objects.filter(playlist=group).order_by('id'):
            userlist.append("http://127.0.0.1:8000/api/users/" + str(user.id))
        return userlist

    def get_tracklist(self, group):
        tracklist = []
        for track in Track.objects.filter(playlist=group).order_by('id'):
            tracklist.append("http://127.0.0.1:8000/api/users/" + str(track.id))
        return tracklist

    class Meta:
        model = Playlist

class UserSerializer(serializers.HyperlinkedModelSerializer):
    scID = serializers.IntegerField()
    permalink = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = User

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    scID = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()  # Time in seconds
    owner = serializers.SerializerMethodField()

    def get_owner(self, group):
        return "http://127.0.0.1:8000/api/users/" + str(User.objects.filter(track=group).order_by('id')[0].id)
    class Meta:
        model = Track

class PlaylistReviewSerializer(serializers.HyperlinkedModelSerializer):
    playlistID = serializers.SerializerMethodField('get_play')
    # user = models.ForeignKey('get_owner')
    date = serializers.DateField()
    review = serializers.CharField(max_length = 1000)

    # def get_owner(self, group):
    #     return "http://127.0.0.1:8000/api/users/" + str(Django_User.objects.filter(group=group).order_by('id')[0].id)

    def get_play(self, group):
        return "http://127.0.0.1:8000/api/playlists/" + str(Django_User.objects.filter(playlistreview=group).order_by('id')[0].id)
    class Meta:
        model = PlaylistReview

class GroupReviewSerializer(serializers.HyperlinkedModelSerializer):
    groupID = serializers.SerializerMethodField('get_play')
    # user = models.ForeignKey('get_owner')
    date = serializers.DateField()
    review = serializers.CharField(max_length = 1000)

    # def get_owner(self, group):
    #     return "http://127.0.0.1:8000/api/users/" + str(Django_User.objects.filter(group=group).order_by('id')[0].id)

    def get_play(self, group):
        return "http://127.0.0.1:8000/api/playlists/" + str(Django_User.objects.filter(groupreview=group).order_by('id')[0].id)
    class Meta:
        model = GroupReview

# class AlbumSerializer(serializers.HyperlinkedModelSerializer):
#     tracks = serializers.SerializerMethodField('get_album_tracks')
#
#     def get_album_tracks(self, album):
#         album_tracks = collections.OrderedDict()
#         num_track = 1
#         for track in Track.objects.filter(album=album):
#             track_url = "http://127.0.0.1:8000/mymusic/api/tracks/" + str(track.id)
#             album_tracks[str(num_track)] = track_url
#             num_track += 1
#         return album_tracks
#
#     class Meta:
#         model = Album
#
# class TrackSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Track