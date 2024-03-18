from rest_framework import generics
from rest_framework.permissions import AllowAny
#from education.models import Module
from users.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from users.serializers import CreateSerializer, PublicListSerializer, LoginSerializer
from django.urls import reverse


class CreateAPIView(generics.CreateAPIView):
    serializer_class = CreateSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class PublicListAPIView(generics.CreateAPIView):
    serializer_class = PublicListSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=self.request, user=serializer.save())
        return redirect(reverse('link-list'))


class LogoutAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = PublicListSerializer

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login-user'))
