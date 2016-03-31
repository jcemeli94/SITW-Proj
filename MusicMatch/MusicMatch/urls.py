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
urlpatterns = [
    url(r'^$', mainpage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get/group/$', views.ListingHTMLGroups, name='get_group'),
    url(r'^get/playlist/$', views.ListingHTMLPlaylists, name='get_playlist'),
    url(r'^get/track/$', views.ListingHTMLTracks, name='get_track'),
    url(r'^get/user/$', views.ListingHTMLUsers, name='get_user'),
    url(r'^get/playlistreview/$', views.ListingHTMLPlaylistReviews, name='get_playlistreview'),
    url(r'^get/groupreview/$', views.ListingHTMLGroupReviews, name='get_groupreview'),
    url(r'^get/group/(?P<objID>[0-9]+)', views.ShowSpecificGroup, name='get_spec_group'),
    url(r'^get/playlist/(?P<objID>[0-9]+)', views.ShowSpecificPlaylist, name='get_spec_playlist'),
    url(r'^get/track/(?P<objID>[0-9]+)', views.ShowSpecificTrack, name='get_spec_track'),
    url(r'^get/user/(?P<objID>[0-9]+)', views.ShowSpecificUser, name='get_spec_track'),
    url(r'^get/playlistreview/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistReview, name='get_spec_playlistreview'),
    url(r'^get/groupreview/(?P<objID>[0-9]+)', views.ShowSpecificGroupReview, name='get_spec_groupreview')
]