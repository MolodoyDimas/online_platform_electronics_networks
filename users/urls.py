from django.urls import path
from users.views import (CreateAPIView, LoginAPIView, LogoutAPIView, PublicListAPIView)

urlpatterns = [
    path('create/', CreateAPIView.as_view(), name='user-create'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('logout/', LogoutAPIView.as_view(), name='user-logout'),
    path('publiclist/', PublicListAPIView.as_view(), name='user-publiclist'),
]
