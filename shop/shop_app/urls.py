from django.urls import path
from . import views

from .admin import shop_admin


urlpatterns = [
	path('admin/', shop_admin.urls),
	path('', views.base, name = 'base'),
]