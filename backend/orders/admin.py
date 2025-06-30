from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cart, CartItem, Order # Importa tus modelos

# Registra tus modelos aquí.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)