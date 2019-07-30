from requests import get, post
from django.shortcuts import redirect

def check_stock(request, id):
	host = request.META['HTTP_HOST']
	url = f'http://{host}/api/v1/core/check_product_stock/{id}/'
	print(url)
	result = get_request(url)
	print(result)
	return result


def get_request(url):
	response = get(url).json()
	if response == {"response": True}:
		return True
	else:
		return False

