
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
import json


from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from api.blockchain import substrate
from api.helpers import get_now
 

class TokenViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        token = request.GET.get('token', '')
        task = request.GET.get('task', '')
        
        # things to do
        
        return JsonResponse(response_)

    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        token = request.GET.get('token', '')
        task = request.GET.get('task', '')
        
        # things to do
        
        return JsonResponse(response_)        

