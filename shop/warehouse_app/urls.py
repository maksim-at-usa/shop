from django.urls import path
from . import views
from .admin import warehouse_admin


urlpatterns = [
	path('admin/', warehouse_admin.urls),
	path('', views.base, name = 'base'),
]