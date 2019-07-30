from django.http import JsonResponse
from shop_app.models import ShopProduct
from warehouse_app.models import WarehouseProduct

from .api_decorators import (
 	Check
)

from .api_utils import check_stock



@Check.get
@Check.product_id
def check_product_stock(request, product_id):
	if WarehouseProduct.objects.get(id=product_id).in_stock:
		return JsonResponse({"response": True})
	else:
		return JsonResponse({"response": False})

