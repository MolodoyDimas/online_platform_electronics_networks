from django.urls import path
from users import views

urlpatterns = [
    path('create/', views.CreateAPIView.as_view(), name='user-create'),
    path('login/', views.CreateAPIView.as_view(), name='user-login'),
    path('logout/', views.CreateAPIView.as_view(), name='user-logout'),
    path('publiclist/', views.CreateAPIView.as_view(), name='user-publiclist'),
]
