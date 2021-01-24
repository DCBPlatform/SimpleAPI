
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
import json


from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from api.blockchain import substrate
 

class GenerateKeyViews(APIView):

    def get(self, request, format=None):
        
        # task = request.GET.get('task', '')
        
        mnemonic = Keypair.generate_mnemonic()
        keypair = Keypair.create_from_mnemonic(mnemonic)
        
        response_ = {
            'mnemonic': mnemonic, 
            'address': keypair.ss58_address,
            'public_key': keypair.public_key,
            'private_key': keypair.private_key,
        }
        return Response(response_)


class KeySignViews(APIView):

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
        return Response(response_)


class KeyVerifyViews(APIView):

    def post(self, request, format=None):
        
        _data = json.loads(request.body)
        message = _data['message']
        signature = _data['signature']
        address = _data['address']

        keypair = Keypair(ss58_address=address)
        result = keypair.verify(message, signature)

        response_ = {}
        response_['address'] = address
        response_['message'] = message
        response_['valid'] = result
        return Response(response_)

