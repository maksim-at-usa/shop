from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, WarehouseProductSerializer

from warehouse_app.models import (
	WarehouseProduct,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WarehouseProductiewSet(viewsets.ModelViewSet):
	queryset = WarehouseProduct.objects.all()
	serializer_class = WarehouseProductSerializer