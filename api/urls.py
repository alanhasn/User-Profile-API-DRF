from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import ListUserProfileView , DetailUserProfileView

urlpatterns = [
    path("api/users-profile", ListUserProfileView.as_view() , name="list-user-profile"),
    path("api/users-profile/<int:pk>", DetailUserProfileView.as_view() , name='detail-user-profile'),

    # JWT Auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
