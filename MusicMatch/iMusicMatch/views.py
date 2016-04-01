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

def ListingXMLGroups(request):
    data = serializers.serialize("xml", Group.objects.all())
    return HttpResponse(data,content_type='application/xml')

def ListingXMLPlaylists(request):
    data = serializers.serialize("xml", Playlist.objects.all())
    return HttpResponse(data,content_type='application/xml')

def ListingXMLTracks(request):
    data = serializers.serialize("xml", Track.objects.all())
    return HttpResponse(data,content_type='application/xml')

def ListingXMLUsers(request):
    data = serializers.serialize("xml", User.objects.all())
    return HttpResponse(data,content_type='application/xml')

def ListingXMLPlaylistReviews(request):
    data = serializers.serialize("xml", PlaylistReview.objects.all())
    return HttpResponse(data,content_type='application/xml')

def ListingXMLGroupReviews(request):
    data = serializers.serialize("xml", GroupReview.objects.all())
    return HttpResponse(data,content_type='application/xml')



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


# JSON

def ListingJSONGroups(request):
    data = serializers.serialize("json", Group.objects.all())
    return HttpResponse(data, content_type='application/json')

def ListingJSONTracks(request):
    data = serializers.serialize("json", Track.objects.all())
    return HttpResponse(data, content_type='application/json')

def ListingJSONPlaylists(request):
    data = serializers.serialize("json", Playlist.objects.all())
    return HttpResponse(data, content_type='application/json')

def ListingJSONUsers(request):
    data = serializers.serialize("json", User.objects.all())
    return HttpResponse(data, content_type='application/json')

def ListingJSONPlaylistReviews(request):
    data = serializers.serialize("json", PlaylistReview.objects.all())
    return HttpResponse(data, content_type='application/json')

def ListingJSONGroupReviews(request):
    data = serializers.serialize("json", GroupReview.objects.all())
    return HttpResponse(data, content_type='application/json')