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

    url(r'^api/$', include(router.urls)),
    url(r'^api/groups/$',
        views.GroupsApiList.as_view(), name="group-list"),
    url(r'^api/groups/(?P<pk>\d+)/$',
        GroupsApiDetail.as_view(), name="group-detail"),
    url(r'^api/playlists/$',
        views.PlaylistsApiList.as_view(), name="playlist-list"),
    url(r'^api/playlists/(?P<pk>\d+)/$',
        PlaylistsApiDetail.as_view(), name="playlist-detail"),
    url(r'^api/users/$',
        views.UsersApiList.as_view(), name="user-list"),
    url(r'^api/users/(?P<pk>\d+)/$',
        UsersApiDetail.as_view(), name="user-detail"),
    url(r'^api/tracks/$',
        views.TracksApiList.as_view(), name="track-list"),
    url(r'^api/tracks/(?P<pk>\d+)/$',
        TracksApiDetail.as_view(), name="track-detail"),
    url(r'^api/groupreviews/$',
        views.GroupReviewsApiList.as_view(), name="groupreview-list"),
    url(r'^api/groupreviews/(?P<pk>\d+)/$',
        GroupReviewsApiDetail.as_view(), name="groupreview-detail"),
    url(r'^api/playlistreviews/$',
        views.PlaylistReviewsApiList.as_view(), name="playlistreview-list"),
    url(r'^api/playlistreviews/(?P<pk>\d+)/$',
        PlaylistReviewsApiDetail.as_view(), name="playlistreview-detail"),

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
    url(r'^playlistreviews.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionPlaylistReviews, name='playlistreview_list'),
    url(r'^groupreviews.(?P<extension>["xml"|"json"]+)/$', views.ListingExtensionGroupReviews, name='groupreview_list'),

    url(r'^groups.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',    views.ShowSpecificGroupExtension,    name='group_detail'),
    url(r'^playlists.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)', views.ShowSpecificPlaylistExtension, name='playlist_detail'),
    url(r'^tracks.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',    views.ShowSpecificTrackExtension,    name='track_detail'),
    url(r'^users.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',     views.ShowSpecificUserExtension,     name='user_detail'),
    url(r'^playlistreviews.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',  views.ShowSpecificPlaylistReviewExtension, name='playlistreview_detail'),
    url(r'^groupreviews.(?P<extension>["xml"|"json"]+)/(?P<objID>[0-9]+)',     views.ShowSpecificGroupReviewExtension,    name='groupreview_detail'),

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
    url(r'^api_soundcloud_random/$', views.api_soundcloud_random, name='api_soundcloud_random'),
    url(r'^api_soundcloud_userHeuristic/$', views.api_soundcloud_userHeuristic, name='api_soundcloud_userHeuristic'),

]