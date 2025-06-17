from django.db import models

# Modelo para las categorías de productos
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Nombre único de la categoría
    description = models.TextField(blank=True, null=True) # Descripción opcional

    class Meta:
        verbose_name_plural = "Categories" # Ayuda en el panel de administración

    def __str__(self):
        return self.name # Representación legible del objeto

# Modelo para los productos individuales
class Product(models.Model):
    name = models.CharField(max_length=200) # Nombre del producto
    description = models.TextField(blank=True, null=True) # Descripción detallada
    price = models.DecimalField(max_digits=10, decimal_places=2) # Precio (ej: 99999999.99)
    stock = models.IntegerField(default=0) # Cantidad disponible en inventario
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    # foreign key a Category: si una categoría se borra, los productos se quedan pero su categoría se pone a NULL
    # related_name='products' permite acceder a productos de una categoría: category.products.all()
    image_url = models.URLField(max_length=500, blank=True, null=True) # URL de la imagen del producto

    def __str__(self):
        return self.name # Representación legible del objeto