from chatback.models import *
from rest_framework.renderers import *
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.views.generic.simple import direct_to_template

def Index(request):

    return direct_to_template(request, '../chatterbox/app/index.html', {})


"""
    DRF functions
"""
from rest_framework import generics
from chatback.serializers import *


class RoomList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Requests.
    """
    model = Room
    serializer_class = RoomListSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer)

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Request.
    """
    model = Room
    serializer_class = RoomSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer)

# class StepList(generics.ListCreateAPIView):
#     """
#     API endpoint that represents a list of Requests.
#     """
#     model = Step
#     serializer_class = StepSerializer

# class StepDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API endpoint that represents a single Request.
#     """
#     model = Step
#     serializer_class = StepSerializer