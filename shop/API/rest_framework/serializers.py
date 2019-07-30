from django.contrib.auth.models import User
from rest_framework import serializers

from warehouse_app.models import (
	WarehouseProduct,
)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')

class WarehouseProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = WarehouseProduct
		fields = (
			'id', 'title', '_article', '_type',
			'price', 'in_stock'
		)
