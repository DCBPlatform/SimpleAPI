
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from api.blockchain import substrate
from api.helpers import get_now
 

class ExtrinsicViews(APIView):

    def post(self, request, format=None):

        _data = request.data 
        key = _data.key
        module = _data.module
        function = _data.function
        params = _data.params

        keypair = Keypair.create_from_private_key(key)

        call = substrate.compose_call(
            call_module=module,
            call_function=function,
            call_params=params
        )

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)   
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        response_ = {}
        response_['extrinsic'] = extrinsic     
        response_['receipt'] = receipt  
        response_['timestamp'] = get_now()   
        return JsonResponse(response_)

class StorageViews(APIView):

    def get(self, request, format=None):

        _data = request.data 
        module = _data.module
        function = _data.function
        params = _data.params
        block_hash = _data.block_hash

        if block_hash:
            result = substrate.query(
                module=module,
                storage_function=function,
                params=params,
                block_hash=block_hash
            )
        else:

            result = substrate.query(
                module=module,
                storage_function=function,
                params=params
            )

        response_ = {}
        response_['result'] = result
        response_['timestamp'] = get_now()
        return JsonResponse(response_)