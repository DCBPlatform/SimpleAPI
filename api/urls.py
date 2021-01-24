from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url

from django.db.models.sql import datastructures
from django.core.exceptions import EmptyResultSet

datastructures.EmptyResultSet = EmptyResultSet

# from rest_framework import routers
# from rest_framework_extensions.routers import NestedRouterMixin

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

# # from users.views import (
# #     MyTokenObtainPairView
# # )

from chains import views as chain_views
from keys import views as key_views


urlpatterns = [

    url('v1/chains/extrinsics', chain_views.ExtrinsicViews.as_view()),
    url('v1/chains/storage', chain_views.StorageViews.as_view()),

    url('v1/keys/generate', key_views.GenerateKeyViews.as_view()),
    url('v1/keys/sign', key_views.KeySignViews.as_view()),
    url('v1/keys/verify', key_views.KeyVerifyViews.as_view()),
    # url(r'v1/', include(router.urls)),
    # url(r'auth/', include('rest_auth.urls')),
    # url(r'auth/registration/', include('rest_auth.registration.urls')),

    # #url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]