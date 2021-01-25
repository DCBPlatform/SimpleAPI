
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
 

class GenerateWalletViews(APIView):

    def get(self, request, format=None):    
        
        mnemonic = Keypair.generate_mnemonic()
        keypair = Keypair.create_from_mnemonic(mnemonic)
        
        response_ = {
            'mnemonic': mnemonic, 
            'address': keypair.ss58_address,
            'public_key': keypair.public_key,
            'private_key': keypair.private_key,
        }
        response_['timestamp'] = get_now()
        return JsonResponse(response_)

class WalletBalanceViews(APIView):

    def get(self, request, format=None):

        account = request.GET.get('account', '')
        response_ = {}
        response_['timestamp'] = get_now()

        if account:
            pass
        else: 
            response_['error_message'] = 'Account ID is not provided in params'
            return JsonResponse(response_)

        result = substrate.query(
            module='System',
            storage_function='Account',
            params=[account]
        )        

        response_['result'] = result.value
        return JsonResponse(response_)


    def post(self, request, format=None):

        _data = json.loads(request.body)
        response_ = {}
        response_['timestamp'] = get_now()

        amount = float(_data['amount']) * 10**12
        receipient = _data['receipient']
        address = _data['address']
        key = _data['private_key']

        keypair = Keypair.create_from_private_key(key, ss58_address=address)

        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': receipient,
                'value': amount
            }
        )       

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair) 
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

        response_['block_hash'] = receipt.block_hash
        response_['extrinsic_hash'] = receipt.extrinsic_hash

        return JsonResponse(response_)        

class WalletSignViews(APIView):

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
        response_['timestamp'] = get_now()
        return JsonResponse(response_)


class WalletVerifyViews(APIView):

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
        response_['timestamp'] = get_now()
        return JsonResponse(response_)

