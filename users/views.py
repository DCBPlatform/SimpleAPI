from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['user_type'] = user.user_type

        return token

class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status, generics

from django_filters.rest_framework import DjangoFilterBackend

from users.models import (
    CustomUser
)

from users.serializers import (
    CustomUserSerializer,
    RegisterSerializer
)

class RegisterViews(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_fields = [
#         'email',
#     ]

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny]
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    

    
#     def get_queryset(self):
#         queryset = CustomUser.objects.all()
#         return queryset   