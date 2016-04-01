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

    url(r'^get/html/group/$',           views.ListingHTMLGroups,     name='get_group'),
    url(r'^get/html/playlist/$',        views.ListingHTMLPlaylists,  name='get_playlist'),
    url(r'^get/html/track/$',           views.ListingHTMLTracks,     name='get_track'),
    url(r'^get/html/user/$',            views.ListingHTMLUsers,      name='get_user'),
    url(r'^get/html/playlistreview/$',  views.ListingHTMLPlaylistReviews,    name='get_playlistreview'),
    url(r'^get/html/groupreview/$',     views.ListingHTMLGroupReviews,       name='get_groupreview'),
    url(r'^get/html/group/(?P<objID>[0-9]+)',    views.ShowSpecificGroup,    name='get_spec_group'),
    url(r'^get/html/playlist/(?P<objID>[0-9]+)', views.ShowSpecificPlaylist, name='get_spec_playlist'),
    url(r'^get/html/track/(?P<objID>[0-9]+)',    views.ShowSpecificTrack,    name='get_spec_track'),
    url(r'^get/html/user/(?P<objID>[0-9]+)',     views.ShowSpecificUser,     name='get_spec_track'),
    url(r'^get/html/playlistreview/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReview, name='get_spec_playlistreview'),
    url(r'^get/html/groupreview/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReview,    name='get_spec_groupreview'),


    url(r'^get/xml/group/$',     views.ListingXMLGroups,    name='get_group'    ),
    url(r'^get/xml/playlist/$',  views.ListingXMLPlaylists, name='get_playlist' ),
    url(r'^get/xml/track/$',     views.ListingXMLTracks,    name='get_track'    ),
    url(r'^get/xml/user/$',      views.ListingXMLUsers,     name='get_user'     ),
    url(r'^get/xml/playlistreview/$',  views.ListingXMLPlaylistReviews,    name='get_playlistreview'),
    url(r'^get/xml/groupreview/$',     views.ListingXMLGroupReviews,       name='get_groupreview'),

    url(r'^get/xml/group/(?P<objID>[0-9]+)',    views.ShowSpecificGroupXML,    name='get_spec_group'),
    url(r'^get/xml/playlist/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistXML, name='get_spec_playlist'),
    url(r'^get/xml/track/(?P<objID>[0-9]+)',    views.ShowSpecificTrackXML,    name='get_spec_track'),
    url(r'^get/xml/user/(?P<objID>[0-9]+)',     views.ShowSpecificUserXML,     name='get_spec_track'),
    url(r'^get/xml/playlistreview/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReviewXML, name='get_spec_playlistreview'),
    url(r'^get/xml/groupreview/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReviewXML,    name='get_spec_groupreview'),


    url(r'^get/json/group/$', views.ListingJSONGroups, name='get_group'),
    url(r'^get/json/track/$', views.ListingJSONTracks, name='get_track'),
    url(r'^get/json/playlist/$', views.ListingJSONPlaylists, name='get_playlist'),
    url(r'^get/json/user/$', views.ListingJSONUsers, name='get_user'),
    url(r'^get/json/groupreview/$', views.ListingJSONGroupReviews, name='get_groupreview'),
    url(r'^get/json/playlistreview/$', views.ListingJSONPlaylistReviews, name='get_playlistreview'),

    url(r'^get/json/group/(?P<objID>[0-9]+)',    views.ShowSpecificGroupJSON,    name='get_spec_group'),
    url(r'^get/json/playlist/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistJSON, name='get_spec_playlist'),
    url(r'^get/json/track/(?P<objID>[0-9]+)',    views.ShowSpecificTrackJSON,    name='get_spec_track'),
    url(r'^get/json/user/(?P<objID>[0-9]+)',     views.ShowSpecificUserJSON,     name='get_spec_track'),
    url(r'^get/json/playlistreview/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReviewJSON, name='get_spec_playlistreview'),
    url(r'^get/json/groupreview/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReviewJSON,    name='get_spec_groupreview'),

]