from rest_framework_simplejwt.tokens import RefreshToken



from django.http import Http404, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend


import os
import json

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class CustomTokenObtainViews(APIView):

    def get(self, request, format=None):  
        refresh = RefreshToken.for_user('1')

        response_ = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return JsonResponse(response_)