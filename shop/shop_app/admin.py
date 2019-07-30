from django.contrib import admin
from .models import (
	ShopProduct, Order, Promotion, Personal
)
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.models import User
#from .admin_custom import ShopAdminSite
# Register your models here.

class ShopAdminSite(AdminSite):
	pass

shop_admin = ShopAdminSite(name='shop_admin')

shop_admin.site_header = 'Shop administration v0.1'
shop_admin.index_title = 'Shop'
shop_admin.site_title = 'Shop'

@admin.register(Promotion)
class Promotion(admin.ModelAdmin):
	pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = (
		'id', 'title', 'customer', 'is_active',
		'is_valid', 'is_canceled', 'is_stoped',
		'is_payed', 'is_delivered'
	)
	list_filter = (
		'is_active','is_valid', 'is_canceled',
		'is_stoped', 'is_payed', 
	)
	search_fields = ('title', 'customer')
	filter_horizontal = ('basket',)

	fieldsets = (
		("Order info", {
			'fields': (
				'title', 'customer', 'is_active',
				'is_valid', 'is_canceled', 'is_stoped',
				'is_payed', 'basket' , 'full_price'
			),
		}),
	)

@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
	list_display = ('id', '_type', 'price', 'in_stock')
	list_filter = ('_type', 'in_stock')
	search_fields = ('title',)

	filter_horizontal = ('promotions',)

	fieldsets = (
		("Product info", {
			'fields': (
				'promotions', 
			),
		}),
		("Warehouse info", {
			'classes': ('collapse',),
			'fields': (
				'title', '_type', 'price', '_article',
				'description', 'in_stock', 
			),
		}),
	)