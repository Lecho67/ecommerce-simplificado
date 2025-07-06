from rest_framework import serializers
from .models import Product, Category # Importa tus modelos

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # Incluye todos los campos del modelo Category

class ProductSerializer(serializers.ModelSerializer):
    # Permite mostrar el nombre de la categoría en lugar de solo su ID
    # read_only=True significa que este campo se leerá de la DB pero no se usará para crear/actualizar productos
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_name', 'image_url']
        # 'category' se usará para enviar el ID de la categoría al crear/actualizar
        # 'category_name' solo para visualización
        read_only_fields = ['category_name']