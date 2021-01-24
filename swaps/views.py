
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
 

class PairViews(APIView):

    def get(self, request, format=None):
        
        # task = request.GET.get('task', '')
        
        mnemonic = Keypair.generate_mnemonic()
        keypair = Keypair.create_from_mnemonic(mnemonic)
        
        response_ = {}
        response_['timestamp'] = get_now()
        response_['pairs'] = []
        return JsonResponse(response_)


class PairDetailViews(APIView):

    def post(self, request, format=None):

        _data = json.loads(request.body)
        message = _data['message']
        key = _data['key']
        address = _data['address']
        keypair = Keypair.create_from_private_key(key, ss58_address=address)
        signature = keypair.sign(message)

        response_ = {}
        response_['address'] = address
        response_['message'] = message
        response_['signature'] = signature
        return JsonResponse(response_)

