from django.contrib import admin
from django.urls import path, include # Importa las funciones necesarias para manejar las URLs

urlpatterns = [
    path('admin/', admin.site.urls), # URL del panel de administración de Django
    path('api/', include('products.urls')), # Incluye las URLs de la app 'products' bajo el prefijo '/api/'
    path('api/', include('orders.urls')),   # Incluye las URLs de la app 'orders' bajo el prefijo '/api/'
]