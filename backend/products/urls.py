from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet # Importa tus ViewSets

# Crea un router
router = DefaultRouter()
# Registra tus ViewSets con el router. El primer argumento es el prefijo de la URL.
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

# Las urlpatterns incluyen las URL generadas por el router
urlpatterns = [
    path('', include(router.urls)),
]