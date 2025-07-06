from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- AÑADE ESTA LÍNEA
from django.conf.urls.static import static # <-- AÑADE ESTA LÍNEAmport path, include # Asegúrate de que 'include' esté aquí

urlpatterns = [
    path('admin/', admin.site.urls), # URL del panel de administración de Django
    path('api/', include('products.urls')), # Incluye las URLs de productos bajo el prefijo '/api/'
    path('api/', include('orders.urls')),   # Incluye las URLs de órdenes bajo el prefijo '/api/'
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)