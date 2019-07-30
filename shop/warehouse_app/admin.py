from django.contrib import admin
from shop_app.models import ShopProduct
from warehouse_app.models import WarehouseProduct
from django.contrib.admin import AdminSite
#from .admin_custom import WarehouseAdminSite
# Register your models here.

class WarehouseAdminSite(AdminSite):
	pass

warehouse_admin = WarehouseAdminSite(name='warehouse_admin')

warehouse_admin.site_header = 'Warehouse administration v0.1'
warehouse_admin.index_title = 'Warehouse'
warehouse_admin.site_title = 'Warehouse'

#warehouse_admin.register(WarehouseProduct)
@admin.register(WarehouseProduct)
class WarehouseProductAdmin(admin.ModelAdmin):
	pass
#warehouse_admin.unregister(auth)