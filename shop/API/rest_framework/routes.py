from rest_framework import routers
from .views import UserViewSet, WarehouseProductiewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('warehouse_products', WarehouseProductiewSet)