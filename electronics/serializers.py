from rest_framework import serializers, viewsets

from electronics.models import NetworkNode
from rest_framework import permissions


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = SupplierSerializer


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверка, является ли пользователь активным сотрудником
        return request.user.is_active_employee


# Пример настройки прав доступа для представлений
class NetworkNodeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsActiveEmployee]


class NetworkNodeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeUpdateSerializer