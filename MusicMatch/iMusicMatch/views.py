from django.shortcuts import render
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
    gps = Group.objects.filter(scID__exact=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLGroup.html', {'gps':gps})

def ShowSpecificPlaylist(request, objID):
    playl = Playlist.objects.filter(scID__exact=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLPlaylist.html', {'playl':playl})

def ShowSpecificTrack(request, objID):
    trs = Track.objects.filter(scID__exact=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLTrack.html', {'trs': trs})

def ShowSpecificUser(request, objID):
    usrs = User.objects.filter(scID__exact=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLUser.html', {'usrs': usrs})

def ShowSpecificPlaylistReview(request, objID):
    rvs = PlaylistReview.objects.filter(scID__exact=objID)
    return render(request, 'iMusicMatch/ListingHTMLPlaylistReview.html', {'rvs': rvs})

def ShowSpecificGroupReview(request, objID):
    rvs = GroupReview.objects.filter(scID__exact=objID)
    return render(request, 'iMusicMatch/ListingHTMLGroupReview.html', {'rvs': rvs})