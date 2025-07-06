from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderViewSet # Importa tus ViewSets

# Crea un router
router = DefaultRouter()
# Registra tus ViewSets
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)

# Las urlpatterns incluyen las URL generadas por el router
urlpatterns = [
    path('', include(router.urls)),
]