
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
