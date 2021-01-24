
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from api.blockchain import substrate
 

class ContractViews(APIView):

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
        
        # task = request.GET.get('task', '')

        _data = request.data 
        message = _data.message
        signature = _data.signature
        address = _data.address

        response_ = {}
        return Response(response_)


class KeyVerifyViews(APIView):

    def post(self, request, format=None):
        
        # task = request.GET.get('task', '')
        
        _data = request.data 
        message = _data.message
        signature = _data.signature
        address = _data.address

        response_ = {}
        
        response_ = {}
        return Response(response_)

