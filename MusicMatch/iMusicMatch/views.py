from django.shortcuts import *
from django.core.serializers import serialize
from django.http import *
from django.utils import timezone
from django.shortcuts import redirect
from forms import *
from .models import User as App_User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import *
import json

from rest_framework import generics
from restDir.serializers import *

import requests


from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerializer, GroupSerializer

clientKey = "887b335a80f3e625454ebca548c53d96"

def mainpage(request):
    return render(request, 'iMusicMatch/mainPage.html')


def api_soundcloud(request):
    return render(request, 'iMusicMatch/api/api_soundcloud.html')

def api_soundcloud_random(request):
    return render(request, 'iMusicMatch/api/api_soundcloud_random.html')

def api_soundcloud_userHeuristic(request):
    return render(request, 'iMusicMatch/api/api_soundcloud_userHeuristic.html')

def ListEntity(request, basename, entityType, entitys):
    return render(request, 'iMusicMatch/ListingEntity.html', {'basename':basename,'entitys': entitys, 'entityType': entityType})


def ListingHTMLGroups(request):
    entitys = Group.objects.all()
    print entitys
    return ListEntity(request, "groups", "Group", entitys)

def ListingHTMLPlaylists(request):
    entitys = Playlist.objects.all()
    return ListEntity(request,"playlists", "Playlist", entitys)

def ListingHTMLTracks(request):
    entitys = Track.objects.all()
    return ListEntity(request, "tracks", "Track", entitys)

def ListingHTMLUsers(request):
    entitys = App_User.objects.all()
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
    usrs = App_User.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLUser.html', {'usrs': usrs})

def ShowSpecificPlaylistReview(request, objID):
    rvs = PlaylistReview.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLPlaylistReview.html', {'rvs': rvs})

def ShowSpecificGroupReview(request, objID):
    rvs = GroupReview.objects.filter(id=int(objID))
    return render(request, 'iMusicMatch/ListingHTMLGroupReview.html', {'rvs': rvs})


# XML

def ListingExtensionGroups(request, extension):
    data = serialize(extension, Group.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionPlaylists(request, extension):
    data = serialize(extension, Playlist.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionTracks(request, extension):
    data = serialize(extension, Track.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionUsers(request, extension):
    data = serialize(extension, App_User.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionPlaylistReviews(request, extension):
    data = serialize(extension, PlaylistReview.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)

def ListingExtensionGroupReviews(request, extension):
    data = serialize(extension, Group.objects.all())
    contType = 'application/', extension
    return HttpResponse(data,content_type=contType)



def ShowSpecificGroupExtension(request, extension, objID):
    gps =serialize(extension, Group.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(gps,content_type=contType)

def ShowSpecificPlaylistExtension(request, extension, objID):
    playl =serialize(extension, Playlist.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(playl,content_type=contType)

def ShowSpecificTrackExtension(request, extension, objID):
    trs = serialize(extension, Track.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(trs,content_type=contType)

def ShowSpecificUserExtension(request, extension, objID):
    usrs =serialize(extension, App_User.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(usrs,content_type=contType)

def ShowSpecificPlaylistReviewExtension(request, extension, objID):
    rvs =serialize(extension, PlaylistReview.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(rvs,content_type=contType)

def ShowSpecificGroupReviewExtension(request, extension, objID):
    rvs =serialize(extension, GroupReview.objects.filter(id=int(objID)))
    contType = 'application/', extension
    return HttpResponse(rvs,content_type=contType)



#Inserts

@login_required
def NewGroupReview(request):
    tList =[]
    uList = []
    if request.method == "POST":
        form = PostFormGroupReview(request.POST)
        formGroup = PostFormGroup(request.POST)
        try:
            post = Group.objects.filter(name=formGroup.instance.name)[0]
        except:
            response = requests.get("http://api.soundcloud.com/groups/?permalink="+formGroup.instance.name\
                                        +"&client_id="+clientKey)
            r = json.loads(response.text)
            formGroup.instance.scID = int(r[0]["id"])
            formGroup.id= int(r[0]["id"])
            post = formGroup.save(commit=False)
            print post
            post.published_date = timezone.now()
            post.save()
            for user in xrange(10):
                try:
                    r[0]['users'][user]['permalink'].decode('ascii')
                    r[0]['users'][user]['username'].decode('ascii')
                    try:
                        u=App_User.objects.filter(permalink=r[0]['users'][user]['permalink'].decode('ascii'))[0]
                    except:
                        u = App_User(id=r[0]['users'][user]['id'],
                                     scID=r[0]['users'][user]['id'],
                                     permalink=r[0]['users'][user]['permalink'],
                                     name=r[0]['users'][user]['username'])
                        u.save()
                    uList.append(u)
                except:
                    print "Error creating user"


            for track in xrange(10):
                try:
                    try:
                        u=App_User.objects.filter(permalink=r[0]['tracks'][track]['user']['permalink'])[0]
                    except:
                        r[0]['tracks'][track]['user']['permalink'].decode('ascii')
                        r[0]['tracks'][track]['user']['username'].decode('ascii')
                        u = App_User(id=r[0]['tracks'][track]['user']['id'],
                                     scID=r[0]['tracks'][track]['user']['id'],
                                     permalink=r[0]['tracks'][track]['user']['permalink'],
                                     name=r[0]['tracks'][track]['user']['username'])
                        u.save()
                    r[0]['tracks'][track]['title'].decode('ascii')
                    try:
                        t=Track.objects.filter(scID=r[0]['tracks'][track]['id'])[0]
                    except:
                        t = Track(
                            id=r[0]['tracks'][track]['id'],
                            scID=r[0]['tracks'][track]['id'],
                            name=r[0]['tracks'][track]['title'],
                            duration=r[0]['tracks'][track]['duration'],
                            owner=u)
                        t.save()
                    tList.append(t)
                except:
                    print "Error creating"
        form.instance.date = datetime.today()
        form.instance.user = request.user
        try:
            form.instance.groupID = post
        except:
            form.instance.groupID = post.instance
        post = form.save(commit=False)
        post.published_date = timezone.now()
        post.save()
        cPlay = Group.objects.filter(groupreview=form.instance)[0]
        for t in tList:
            cPlay.trackList.add(t)
        for u in uList:
            cPlay.members.add(u)
        return redirect('http://127.0.0.1:8000/')  # canviar URL
    else:
        form = PostFormGroupReview()
        formGroup = PostFormGroup()
    return render(request, 'iMusicMatch/post/NewGroupReview.html', {'form': form, 'formGroup' : formGroup})

@login_required
def NewPlaylistReview(request):
    tList = []
    uList = []
    if request.method == "POST":
        form = PostFormPlaylistReview(request.POST)
        formPlaylist = PostFormPlaylist(request.POST)
        if form.is_valid() and formPlaylist.is_valid():
            try:
                post = Playlist.objects.filter(name=formPlaylist.instance.name)[0]
            except IndexError:
                response = requests.get("http://api.soundcloud.com/playlists/?permalink=" + formPlaylist.instance.name \
                                        + "&client_id=" + clientKey)
                r = json.loads(response.text)
                try:
                    print r[0]['tracks']
                    print r[0]['tracks'][0]['title']
                    print r[0]['tracks'][0]['id']
                except:
                    print "Out of range"
                formPlaylist.instance.scID = int(r[0]["id"])
                formPlaylist.id = int(r[0]["id"])
                post = formPlaylist.save(commit=False)
                print post
                post.published_date = timezone.now()
                post.save()
                for track in xrange(10):
                    try:
                        try:
                            u = App_User.objects.filter(permalink=r[0]['tracks'][track]['user']['permalink'])[0]
                        except:
                            r[0]['tracks'][track]['user']['permalink'].decode('ascii')
                            r[0]['tracks'][track]['user']['username'].decode('ascii')
                            u = App_User(id=r[0]['tracks'][track]['user']['id'],
                                         scID=r[0]['tracks'][track]['user']['id'],
                                         permalink=r[0]['tracks'][track]['user']['permalink'],
                                         name=r[0]['tracks'][track]['user']['username'])
                            u.save()
                        r[0]['tracks'][track]['title'].decode('ascii')
                        try:
                            t = Track.objects.filter(scID=r[0]['tracks'][track]['id'])[0]
                        except:
                            t = Track(
                                id=r[0]['tracks'][track]['id'],
                                scID=r[0]['tracks'][track]['id'],
                                name=r[0]['tracks'][track]['title'],
                                duration=r[0]['tracks'][track]['duration'],
                                owner=u)
                            t.save()
                        tList.append(t)
                    except:
                        print "Error creating"
            form.instance.date = datetime.today()
            form.instance.user = request.user
            try:
                form.instance.playlistID = post
            except:
                form.instance.playlistID = post.instance
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            cPlay = Playlist.objects.filter(playlistreview=form.instance)[0]
            for t in tList:
                cPlay.trackList.add(t)
            for u in uList:
                cPlay.members.add(u)

            return redirect('http://127.0.0.1:8000/')  # canviar URL
    else:
        form = PostFormPlaylistReview()
        formPlaylist = PostFormPlaylist()
    return render(request, 'iMusicMatch/post/NewPlaylistReview.html', {'form': form, 'formPlaylist': formPlaylist})

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

#API

class GroupsApiList(generics.ListCreateAPIView):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializerAPI

class GroupsApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializerAPI

class PlaylistsApiList(generics.ListCreateAPIView):
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistsApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class UsersApiList(generics.ListCreateAPIView):
    model = App_User
    queryset = App_User.objects.all()
    serializer_class = UserSerializerAPI

class UsersApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = App_User
    queryset = App_User.objects.all()
    serializer_class = UserSerializerAPI

class TracksApiList(generics.ListCreateAPIView):
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TracksApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class PlaylistReviewsApiList(generics.ListCreateAPIView):
    model = PlaylistReview
    queryset = PlaylistReview.objects.all()
    serializer_class = PlaylistReviewSerializer

class PlaylistReviewsApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PlaylistReview
    queryset = PlaylistReview.objects.all()
    serializer_class = PlaylistReviewSerializer

class GroupReviewsApiList(generics.ListCreateAPIView):
    model = GroupReview
    queryset = GroupReview.objects.all()
    serializer_class = GroupReviewSerializer

class GroupReviewsApiDetail(generics.RetrieveUpdateDestroyAPIView):
    model = GroupReview
    queryset = GroupReview.objects.all()
    serializer_class = GroupReviewSerializer