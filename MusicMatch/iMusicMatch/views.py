from django.shortcuts import *
from django.core import serializers
from django.http import *
from django.utils import timezone
from django.shortcuts import redirect
from forms import *
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
    return render(request, 'iMusicMatch/NewGroup.html', {'form': form})



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
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
     # Attempt to grab information from the raw form information.
     # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

            # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
                # Save the user's form data to the database.
            user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

                # Did the user provide a profile picture?
                # # If so, we need to get it from the input form and put it in the UserProfile model.
                # if 'realName' in request.FILES:
                #     profile.realName = request.FILES['realName']

                # Now we save the UserProfile model instance.
            profile.save()

                # Update our variable to tell the template registration was successful.
            registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

        # Render the template depending on the context.
    return render_to_response(
        'iMusicMatch/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)

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