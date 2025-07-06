from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer # Importa tus serializadores

# ViewSet para las Categorías
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # Define qué objetos se van a manejar
    serializer_class = CategorySerializer # Define qué serializador se va a usar
    # ModelViewSet proporciona automáticamente los endpoints para:
    # GET /api/categories/ (lista todas)
    # GET /api/categories/{id}/ (obtener una por ID)
    # POST /api/categories/ (crear nueva)
    # PUT/PATCH /api/categories/{id}/ (actualizar)
    # DELETE /api/categories/{id}/ (eliminar)

# ViewSet para los Productos
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Opcional: Filtros y búsqueda (útil para el frontend)
    # from django_filters.rest_framework import DjangoFilterBackend
    # from rest_framework import filters
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['category'] # Permite filtrar por /api/products/?category=<id>
    # search_fields = ['name', 'description'] # Permite buscar por /api/products/?search=<query>
    # Si quieres usar los filtros, deberás instalar 'django-filter': pip install django-filter