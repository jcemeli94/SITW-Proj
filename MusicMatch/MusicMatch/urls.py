"""MusicMatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from iMusicMatch.views import *
from iMusicMatch import views

entityList = ["groups", "playlists", "tracks", "users", "playlistreviews", "groupreviews"]

urlpatterns = [
    url(r'^$', mainpage),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^groups/$',           views.ListingHTMLGroups,     name='get_group'),
    url(r'^playlists/$',        views.ListingHTMLPlaylists,  name='get_playlist'),
    url(r'^tracks/$',           views.ListingHTMLTracks,     name='get_track'),
    url(r'^users/$',            views.ListingHTMLUsers,      name='get_user'),
    url(r'^playlistreviews/$',  views.ListingHTMLPlaylistReviews,    name='get_playlistreview'),
    url(r'^groupreviews/$',     views.ListingHTMLGroupReviews,       name='get_groupreview'),
    url(r'^groups/(?P<objID>[0-9]+)',    views.ShowSpecificGroup,    name='get_spec_group'),
    url(r'^playlists/(?P<objID>[0-9]+)', views.ShowSpecificPlaylist, name='get_spec_playlist'),
    url(r'^tracks/(?P<objID>[0-9]+)',    views.ShowSpecificTrack,    name='get_spec_track'),
    url(r'^users/(?P<objID>[0-9]+)',     views.ShowSpecificUser,     name='get_spec_track'),
    url(r'^playlistreviews/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReview, name='get_spec_playlistreview'),
    url(r'^groupreviews/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReview,    name='get_spec_groupreview'),

    url(r'^groups.(?P<extension>["xml"|"json"]+)/$',     views.ListingExtensionGroups,    name='get_group'),
    url(r'^playlists.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionPlaylists, name='get_playlist'),
    url(r'^tracks.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionTracks, name='get_track'),
    url(r'^users.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionUsers, name='get_user'),
    url(r'^playlistreview.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionPlaylistReviews, name='get_playlistreview'),
    url(r'^groupreviews.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionGroupReviews, name='get_groupreview'),

    url(r'^groups.xml/(?P<objID>[0-9]+)',    views.ShowSpecificGroupXML,    name='get_spec_group'),
    url(r'^playlists.xml/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistXML, name='get_spec_playlist'),
    url(r'^tracks.xml/(?P<objID>[0-9]+)',    views.ShowSpecificTrackXML,    name='get_spec_track'),
    url(r'^users.xml/(?P<objID>[0-9]+)',     views.ShowSpecificUserXML,     name='get_spec_track'),
    url(r'^playlistreviews.xml/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReviewXML, name='get_spec_playlistreview'),
    url(r'^groupreviews.xml/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReviewXML,    name='get_spec_groupreview')

]
#Tests
# url(r'^(?P<entity>["groups"|"playlists"|"tracks"|"users"|"playlistreviews"|"groupreviews"]+).(?P<extension>["xml"|"json"]+)/$', views.ListEntity, name='get_entity'),