
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


from decouple import config

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.helpers import get_now

from payments.models import CardPayment


class PaymentCardViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        # ticker = request.GET.get('tickerId', '')             

        return JsonResponse(response_)

    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        # stripe_ = stripe.Charge.create(
        #     amount=_data['amount'] * 100,
        #     currency="eur",
        #     source=_data['stripeToken'],
        #     description="DCB Wallet")

        # card_payment = CardPayment.objects.create(
        #     email_address=_data['email'],
        #     amount=_data['amount'] * 100,
        #     stripe_id=stripe_.id,
        #     card_id=_data['cardId']
        # )

        return JsonResponse(response_)  
