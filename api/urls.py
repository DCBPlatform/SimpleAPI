from datetime import datetime, timedelta


from django.conf import settings
from django.conf.urls import include, url
from django.db.models.sql import datastructures
from django.core.exceptions import EmptyResultSet
datastructures.EmptyResultSet = EmptyResultSet



from chains import views as chain_views
from swaps import views as swap_views
from tokens import views as token_views
from users import views as user_views
from wallets import views as wallet_views


from rest_framework import routers
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = DefaultRouter()
router.register('wallets', wallet_views.WalletViewSet, basename='wallet')
urlpatterns = router.urls


urlpatterns = [

    url('v1/chains/extrinsics', chain_views.ExtrinsicViews.as_view()),
    url('v1/chains/storage', chain_views.StorageViews.as_view()),

    url('v1/swaps/pairs/', swap_views.PairViews.as_view()),

    url('v1/tokens/', token_views.TokenViews.as_view()),

    url('v1/wallets/balance', wallet_views.WalletBalanceViews.as_view()),
    url('v1/wallets/generate', wallet_views.GenerateWalletViews.as_view()),
    url('v1/wallets/sign', wallet_views.WalletSignViews.as_view()),
    url('v1/wallets/verify', wallet_views.WalletVerifyViews.as_view()),  
    url('v1/wallets/phone', wallet_views.WalletVerifyPhoneViews.as_view()),  

    url('admin/', include(router.urls)),
    url('jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('register/', user_views.RegisterViews.as_view(), name='register'),
    url('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  

]


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


# url(r'v1/', include(router.urls)),
# url(r'auth/', include('rest_auth.urls')),
# url(r'auth/registration/', include('rest_auth.registration.urls')),

# #url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
# url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')