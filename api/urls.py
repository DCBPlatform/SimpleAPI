from datetime import datetime, timedelta


from django.conf import settings
from django.conf.urls import include, url
from django.db.models.sql import datastructures
from django.core.exceptions import EmptyResultSet
datastructures.EmptyResultSet = EmptyResultSet



from chains import views as cv
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

    url('v1/bazaar', cv.BazaarViews.as_view()),
    
    url('v1/bridge', cv.BridgeViews.as_view()),

    url('v1/exchange/orders', cv.ExchangeOrderViews.as_view()),
    url('v1/exchange/pairs', cv.ExchangePairViews.as_view()),

    url('v1/referral', cv.ReferralViews.as_view()),

    url('v1/token', cv.TokenViews.as_view()),

    url('v1/wallet', cv.WalletViews.as_view()),

    # Admin work below....
    url('dcb/', include(router.urls)),
  
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