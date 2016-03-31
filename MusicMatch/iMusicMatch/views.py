from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

from .models import *
#from forms import PostForm #USE FOR FORMULARIES


def mainpage(request):
    #rests = Restaurant.objects.filter(name__isnull=False)
    return render(request, 'iMusicMatch/mainPage.html')
#, {'rests':rests})

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