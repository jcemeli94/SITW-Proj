from django.shortcuts import render
from django.core import serializers
from django.http import *
from django.utils import timezone
from django.shortcuts import redirect

from .models import *
#from forms import PostForm #USE FOR FORMULARIES


def mainpage(request):
    return render(request, 'iMusicMatch/mainPage.html')

def ListingHTMLGroups(request):
    gps = Group.objects.filter(name__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLGroup.html', {'gps': gps})

def ListingHTMLPlaylists(request):
    playl = Playlist.objects.filter(name__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLPlaylist.html', {'playl' : playl})

def ListingHTMLTracks(request):
    trs = Track.objects.filter(name__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLTrack.html', {'trs': trs})

def ListingHTMLUsers(request):
    usrs = User.objects.filter(name__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLUser.html', {'usrs': usrs})

def ListingHTMLPlaylistReviews(request):
    rvs = PlaylistReview.objects.filter(scID__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLPlaylistReview.html', {'rvs': rvs})

def ListingHTMLGroupReviews(request):
    rvs = GroupReview.objects.filter(scID__isnull=False)
    return render(request, 'iMusicMatch/ListingHTMLGroupReview.html', {'rvs': rvs})

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



def ShowSpecificGroupXML(request, objID):
    gps =serializers.serialize("xml", Group.objects.filter(id=int(objID)))
    return HttpResponse(gps,content_type='application/xml')

def ShowSpecificPlaylistXML(request, objID):
    playl =serializers.serialize("xml", Playlist.objects.filter(id=int(objID)))
    return HttpResponse(playl,content_type='application/xml')

def ShowSpecificTrackXML(request, objID):
    trs = serializers.serialize("xml", Track.objects.filter(id=int(objID)))
    return HttpResponse(trs,content_type='application/xml')

def ShowSpecificUserXML(request, objID):
    usrs =serializers.serialize("xml", User.objects.filter(id=int(objID)))
    return HttpResponse(usrs,content_type='application/xml')

def ShowSpecificPlaylistReviewXML(request, objID):
    rvs =serializers.serialize("xml", PlaylistReview.objects.filter(id=int(objID)))
    return HttpResponse(rvs,content_type='application/xml')

def ShowSpecificGroupReviewXML(request, objID):
    rvs =serializers.serialize("xml", GroupReview.objects.filter(id=int(objID)))
    return HttpResponse(rvs,content_type='application/xml')

#Tests

def ListEntity(request, entity, extension):
    print entity
    entity = entity[:-1]
    entity = entity.capitalize()
    print entity
    print extension
    data = serializers.serialize(extension, eval(entity).objects.all())
    print data
    contType = 'application/', extension
    return HttpResponse(data, content_type=contType)