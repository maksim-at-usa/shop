from django.http import JsonResponse

class Check:
	def get(func):
		def wrapper(request, *args, **kwargs):
			if request.method == "GET":
				return func(request, *args, **kwargs)
			else:
				return JsonResponse({"error response": "cant use post method"})
		return wrapper

	def product_id(func):
		def wrapper(request, product_id, *args, **kwargs):
			if product_id:
				return func(request, product_id, *args, **kwargs)
			else:
				return JsonResponse({"error response": "none id"})
		return wrapper