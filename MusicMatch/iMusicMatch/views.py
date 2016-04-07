from django.shortcuts import render
from django.core import serializers
from django.http import *
from django.utils import timezone
from django.shortcuts import redirect

from .models import *
#from forms import PostForm #USE FOR FORMULARIES


def mainpage(request):
    return render(request, 'iMusicMatch/mainPage.html')

def ListEntity(request, basename, entityType, entitys):
    return render(request, 'iMusicMatch/ListingEntity.html', {'basename':basename,'entitys': entitys, 'entityType': entityType})


def ListingHTMLGroups(request):
    entitys = Group.objects.all()
    return ListEntity(request, "groups", "Group", entitys)

def ListingHTMLPlaylists(request):
    entitys = Playlist.objects.all()
    return ListEntity(request,"playlists", "Playlist", entitys)

def ListingHTMLTracks(request):
    entitys = Track.objects.all()
    return ListEntity(request, "tracks", "Track", entitys)

def ListingHTMLUsers(request):
    entitys = User.objects.all()
    return ListEntity(request, "users", "User", entitys)

def ListingHTMLPlaylistReviews(request):
    entitys = PlaylistReview.objects.all()
    return ListEntity(request, "playlistreviews", "Playlist reviews", entitys)

def ListingHTMLGroupReviews(request):
    entitys = GroupReview.objects.all()
    return ListEntity(request, "groupreviews", "Group reviews", entitys)

def ShowSpecificGroup(request, objID):
    gps = Group.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLGroup.html', {'gps':gps})

def ShowSpecificPlaylist(request, objID):
    playl = Playlist.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLPlaylist.html', {'playl':playl})

def ShowSpecificTrack(request, objID):
    trs = Track.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLTrack.html', {'trs': trs})

def ShowSpecificUser(request, objID):
    usrs = User.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLUser.html', {'usrs': usrs})

def ShowSpecificPlaylistReview(request, objID):
    rvs = PlaylistReview.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLPlaylistReview.html', {'rvs': rvs})

def ShowSpecificGroupReview(request, objID):
    rvs = GroupReview.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLGroupReview.html', {'rvs': rvs})


# XML

def ListingExtensionGroups(request, extension):
    data = serializers.serialize(extension, Group.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionPlaylists(request, extension):
    data = serializers.serialize(extension, Playlist.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionTracks(request, extension):
    data = serializers.serialize(extension, Track.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionUsers(request, extension):
    data = serializers.serialize(extension, User.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionPlaylistReviews(request, extension):
    data = serializers.serialize(extension, PlaylistReview.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionGroupReviews(request, extension):
    data = serializers.serialize(extension, Group.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)



def ShowSpecificGroupExtension(request, extension, objID):
    gps =serializers.serialize(extension, Group.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(gps,content_type=contType)

def ShowSpecificPlaylistExtension(request, extension, objID):
    playl =serializers.serialize(extension, Playlist.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(playl,content_type=contType)

def ShowSpecificTrackExtension(request, extension, objID):
    trs = serializers.serialize(extension, Track.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(trs,content_type=contType)

def ShowSpecificUserExtension(request, extension, objID):
    usrs =serializers.serialize(extension, User.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(usrs,content_type=contType)

def ShowSpecificPlaylistReviewExtension(request, extension, objID):
    rvs =serializers.serialize(extension, PlaylistReview.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(rvs,content_type=contType)

def ShowSpecificGroupReviewExtension(request, extension, objID):
    rvs =serializers.serialize(extension, GroupReview.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(rvs,content_type=contType)

#Tests

# def ListEntity(request, entity, extension):
#     print entity
#     entity = entity[:-1]
#     entity = entity.capitalize()
#     print entity
#     print extension
#     data = serializers.serialize(extension, eval(entity).objects.all())
#     print data
#     contType = 'application/', extension
#     return HttpResponse(data, content_type=contType)