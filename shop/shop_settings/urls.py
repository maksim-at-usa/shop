from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from API.rest_framework.routes import router

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
	#path('grappelli/', include('grappelli.urls')), # grappelli URLS

    path('admin/', admin.site.urls),

    # API URLS
    path('api/v1/', include(('API.urls', 'API'), namespace = 'api-urls')),
    
    # [BACKEND] REST API URLS
    path('rest-api/', include(router.urls), name = 'rest-api-urls'),

    # [FRONTEND] SWAGGER API
    path('swagger/', schema_view),

    # SHOP APP URLS
    path('shop/', include(("shop_app.urls", "shop_app"), namespace = 'shop')),

    # WAREHOUSE APP URLS
    path('warehouse/', include(("warehouse_app.urls", "warehouse_app"), namespace = 'warehouse')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


'''
Можно создать обработчик определяющий права авторизованного юзера и в зависимости от его прав,
направлять его на нужный ему роут. Тем самым уменьшив фокус внимания для фронтенда и юзеров и для себя самого,
и обеспечив безопасную работу всех веток апи
'''