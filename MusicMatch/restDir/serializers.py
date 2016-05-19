import collections
from rest_framework import serializers

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
    trackList = serializers.SerializerMethodField('get_tracks')

    def get_userlist(self, group):
        userlist = []
        for user in User.objects.filter(group=group).order_by('id'):
            userlist.append("http://127.0.0.1:8000/api/users/" + str(user.id))
        return userlist

    class Meta:
        model = Playlist


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