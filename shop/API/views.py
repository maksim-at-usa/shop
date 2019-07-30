from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def base(request):
	return JsonResponse({"page": "base client api page"})