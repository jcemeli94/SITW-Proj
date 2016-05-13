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

from django.conf.urls import url, include
from rest_framework import routers
from iMusicMatch import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


entityList = ["groups", "playlists", "tracks", "users", "playlistreviews", "groupreviews"]

urlpatterns = [
    url(r'^$', mainpage),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^groups/$',           views.ListingHTMLGroups,     name='group_list'),
    url(r'^playlists/$',        views.ListingHTMLPlaylists,  name='playlist_list'),
    url(r'^tracks/$',           views.ListingHTMLTracks,     name='track_list'),
    url(r'^users/$',            views.ListingHTMLUsers,      name='user_list'),
    url(r'^playlistreviews/$',  views.ListingHTMLPlaylistReviews,    name='playlistreview_list'),
    url(r'^groupreviews/$',     views.ListingHTMLGroupReviews,       name='groupreview_list'),
    url(r'^groups/(?P<objID>[0-9]+)',    views.ShowSpecificGroup,    name='group_detail'),
    url(r'^playlists/(?P<objID>[0-9]+)', views.ShowSpecificPlaylist, name='get_spec_playlist'),
    url(r'^tracks/(?P<objID>[0-9]+)',    views.ShowSpecificTrack,    name='playlist_detail'),
    url(r'^users/(?P<objID>[0-9]+)',     views.ShowSpecificUser,     name='track_detail'),
    url(r'^playlistreviews/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReview, name='playlistreview_detail'),
    url(r'^groupreviews/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReview,    name='groupreview_detail'),

    url(r'^groups.(?P<extension>["xml"|"json"]+)/$',     views.ListingExtensionGroups,    name='group_list'),
    url(r'^playlists.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionPlaylists, name='playlist_list'),
    url(r'^tracks.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionTracks, name='track_list'),
    url(r'^users.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionUsers, name='user_list'),
    url(r'^playlistreview.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionPlaylistReviews, name='playlistreview_list'),
    url(r'^groupreviews.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionGroupReviews, name='groupreview_list'),

    url(r'^groups.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',    views.ShowSpecificGroupExtension,    name='group_detail'),
    url(r'^playlists.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistExtension, name='playlist_detail'),
    url(r'^tracks.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',    views.ShowSpecificTrackExtension,    name='track_detail'),
    url(r'^users.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',     views.ShowSpecificUserExtension,     name='user_detail'),
    url(r'^playlistreviews.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReviewExtension, name='playlistreview_detail'),
    url(r'^groupreviews.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReviewExtension,    name='groupreview_detail'),

    url(r'^post/new_group/$', views.NewGroup, name='new_group'),
    url(r'^post/new_group_review/$', views.NewGroupReview, name='new_group_review'),
    url(r'^post/new_playlist_review/$', views.NewPlaylistReview, name = 'new_playlist_review'),
    url(r'^edit_playlist_review/(?P<rest_pk>\d+)/$', views.EditPlaylistReview, name='edit_playlist_review'),
    url(r'^edit_group_review/(?P<rest_pk>\d+)/$', views.EditGroupReview, name='edit_group_review'),
    url(r'^delete_group/(?P<rest_pk>\d+)/$', views.delete_group, name='delete_group'),
    url(r'^delete_group_review/(?P<rest_pk>\d+)/$', views.DeleteGroupReview, name='delete_group_review'),
    url(r'^delete_playlist_review/(?P<rest_pk>\d+)/$', views.DeletePlaylistReview, name='delete_playlist_review'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_soundcloud/$', views.api_soundcloud, name='api_soundcloud'),
]

#Insert


#Tests
# url(r'^(?P<entity>["groups"|"playlists"|"tracks"|"users"|"playlistreviews"|"groupreviews"]+).(?P<extension>["xml"|"json"]+)/$', views.ListEntity, name='get_entity'),