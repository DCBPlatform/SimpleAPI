
from django.http import Http404, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend


import os
import json
import stripe

from decouple import config

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.helpers import get_now

class MistertangoHookViews(APIView):


    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        return JsonResponse(response_)  


class StripeHookViews(APIView):


    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        return JsonResponse(response_)  