from datetime import datetime, timedelta


from django.conf import settings
from django.conf.urls import include, url
from django.db.models.sql import datastructures
from django.core.exceptions import EmptyResultSet
datastructures.EmptyResultSet = EmptyResultSet



from chains import views as chain_views
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


    url('v1/exchange/orders', chain_views.ExchangeOrderViews.as_view()),
    url('v1/exchange/pairs', chain_views.ExchangePairViews.as_view()),

    url('v1/token', chain_views.TokenViews.as_view()),

    url('v1/wallet', chain_views.WalletViews.as_view()),

    # Admin work below....
    url('v1/dcb/', include(router.urls)),
  
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