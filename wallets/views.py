
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


from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException


from wallets.models import Wallet
from wallets.serializers import WalletSerializer


from api.helpers import get_now
from api.blockchain import connect
from api.twilio import send_verify_sms, verify_sms

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

        substrate = connect()

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

        substrate = connect()
        
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


class WalletVerifyPhoneViews(APIView):

    def post(self, request, format=None):
        verify = request.GET.get('verify', '')

        _data = json.loads(request.body)
        number = _data['number']
        if verify:
            code = verify
            result = verify_sms(number,code)
        else:
            result = send_verify_sms(number)

        response_ = {}
        response_['result'] = result

        return JsonResponse(response_)



class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Wallet.objects.all()            
        return queryset


    @action(detail=False, methods=['POST'])
    def register(self, request): 

        _data = json.loads(request.body)
        wallet_address = _data['wallet_address']  
        phone = _data['phone']    

        wallet, created = Wallet.objects.get_or_create(
            wallet_address=wallet_address,
            phone=phone
        )
        _response = {
            'wallet': wallet.wallet_address,
            'phone': str(wallet.phone),
            'verified': wallet.verified,
            'id': wallet.id
        }
        return Response(_response)  

    @action(detail=False)
    def view_unverified(self, request):

        wallets = Wallet.objects.filter(verified=False)
        page = self.paginate_queryset(wallets)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(wallets, many=True)
        return Response(serializer.data)               


    @action(detail=True)
    def validate(self, request):
        wallets = Wallet.objects.filter()
        return Response(lol)                       
