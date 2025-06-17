from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer # Importa tus serializadores

# ViewSet para las Categorías
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # Obtiene todas las categorías
    serializer_class = CategorySerializer # Usa el serializador de categorías
    # ModelViewSet proporciona automáticamente los endpoints para:
    # GET /api/categories/ (lista todas)
    # GET /api/categories/{id}/ (obtener una por ID)
    # POST /api/categories/ (crear nueva)
    # PUT/PATCH /api/categories/{id}/ (actualizar)
    # DELETE /api/categories/{id}/ (eliminar)

# ViewSet para los Productos
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() # Obtiene todos los productos
    serializer_class = ProductSerializer    # Usa el serializador de productos
    # Opcional: Filtros y búsqueda (útil para el frontend)
    # from django_filters.rest_framework import DjangoFilterBackend
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['category'] # Permite filtrar por /api/products/?category=<id>
    # search_fields = ['name', 'description'] # Permite buscar por /api/products/?search=<query>
    # Si quieres usar los filtros, deberás instalar 'django-filter': pip install django-filter