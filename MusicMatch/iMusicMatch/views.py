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

#
# def new_restaurant(request):
#         if request.method == "POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.published_date = timezone.now()
#                 post.save()
#                 #return redirect('Restaurantapp/base.html')
#         else:
#             form = PostForm()
#         return render(request, 'Restaurantapp/new_restaurant.html', {'form': form})

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