from django.shortcuts import *
from django.core import serializers
from django.http import *
from django.utils import timezone
from django.shortcuts import redirect
from forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import *
#from forms import PostForm #USE FOR FORMULARIES

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer, GroupSerializer

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



#Inserts

def NewGroup(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('http://127.0.0.1:8000/') #canviar URL
    else:
        form = PostForm()
    return render(request, 'iMusicMatch/post/NewGroup.html', {'form': form})

@login_required
def NewGroupReview(request):
    if request.method == "POST":
        form = PostFormGroupReview(request.POST)
        if form.is_valid():
            form.instance.date = datetime.today()
            form.instance.user = request.user
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('http://127.0.0.1:8000/') #canviar URL
    else:
        form = PostFormGroupReview()
    return render(request, 'iMusicMatch/post/NewGroupReview.html', {'form': form})

@login_required
def NewPlaylistReview(request):
    if request.method == "POST":
        form = PostFormPlaylistReview(request.POST)
        if form.is_valid():
            form.instance.date = datetime.today()
            form.instance.user = request.user
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('http://127.0.0.1:8000/') #canviar URL
    else:
        form = PostFormPlaylistReview()
    return render(request, 'iMusicMatch/post/NewGroupReview.html', {'form': form})

@login_required
def DeleteGroupReview(request, rest_pk):
    delRest = GroupReview.objects.get(pk=rest_pk)
    if delRest.user.__eq__(request.user):
        delRest.delete()
        return render(request, 'iMusicMatch/ListingHTMLGroupReview.html')
    else:
        return render(request, 'iMusicMatch/error/UserNotMatch.html')

@login_required
def DeletePlaylistReview(request, rest_pk):
    delRest = PlaylistReview.objects.get(pk=rest_pk)
    if delRest.user.__eq__(request.user):
        delRest.delete()
        return render(request, 'iMusicMatch/ListingHTMLPlaylistReview.html')
    else:
        return render(request, 'iMusicMatch/error/UserNotMatch.html')


def EditPlaylistReview(request, rest_pk):
    editItem = PlaylistReview.objects.get(pk=rest_pk)
    if editItem.user.__eq__(request.user):
        form = EditPlaylistReviewForm(request.POST)
        if form.is_valid():
            PlaylistReview.objects.filter(pk=rest_pk).update(review=form.instance.review)
            return redirect('http://127.0.0.1:8000/')  # canviar URL
        else:
           form = EditPlaylistReviewForm()
        return render(request, 'iMusicMatch/edit/EditPlaylistReview.html', {'form': form})
    else:
        return render(request, 'iMusicMatch/error/UserNotMatch.html')


def EditGroupReview(request, rest_pk):
    editItem = GroupReview.objects.get(pk=rest_pk)
    if editItem.user.__eq__(request.user):
        form = EditPlaylistReviewForm(request.POST)
        if form.is_valid():
            GroupReview.objects.filter(pk=rest_pk).update(review=form.instance.review)
            return redirect('http://127.0.0.1:8000/')  # canviar URL
        else:
            form = EditGroupReviewForm()
        return render(request, 'iMusicMatch/edit/EditGroupReview.html', {'form': form})
    else:
        return render(request, 'iMusicMatch/error/UserNotMatch.html')

def delete_group(request,rest_pk):
    delRest= Group.objects.get(pk=rest_pk)
    delRest.delete()
    return redirect('http://127.0.0.1:8000/groups/')

def login(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, 'iMusicMatch/login.html', {'form': form})

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
        'iMusicMatch/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)


def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('iMusicMatch/login.html', {}, context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

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