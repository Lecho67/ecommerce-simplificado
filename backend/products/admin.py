from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product # Importa tus modelos

# Registra tus modelos aquí.
admin.site.register(Category)
admin.site.register(Product)