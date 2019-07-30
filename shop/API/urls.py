from django.urls import path, include
from . import views
from .rest_framework import api_views


urlpatterns = [
	path('', views.base, name = 'base'),

	# CORE BACKEND API URLS
	path(
		'core/',
		include(
			('API.rest_framework.urls', 'API'),
			namespace = 'core'
		)
	),
]