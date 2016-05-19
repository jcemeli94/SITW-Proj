from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin
from rest_framework import generics, viewsets

from iMusicMatch.models import *
from restDir.serializers import *


class GroupsApi(viewsets.ReadOnlyModelViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer