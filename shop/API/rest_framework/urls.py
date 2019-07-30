from django.urls import path
from . import api_views 

urlpatterns = [
	path(
		'check_product_stock/<str:product_id>/',
		api_views.check_product_stock,
		name='check-product-stock'
	),
]