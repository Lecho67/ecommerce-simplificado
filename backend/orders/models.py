from django.db import models
from products.models import Product # Importa el modelo Product desde la app 'products'
# from django.contrib.auth.models import User #    autenticación de usuarios

# Modelo para el Carrito de compras
class Cart(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # Si decides implementar usuarios, un carrito por usuario.
    created_at = models.DateTimeField(auto_now_add=True) # Fecha de creación (automático)
    updated_at = models.DateTimeField(auto_now=True) # Fecha de última actualización (automático)

    def __str__(self):
        return f"Cart {self.id}" # Representación legible

# Modelo para los ítems dentro de un Carrito
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    # Foreign key a Cart: si un carrito se borra, sus ítems se borran también
    # related_name='items' permite acceder a los ítems de un carrito: cart.items.all()
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Foreign key al producto
    quantity = models.PositiveIntegerField(default=1) # Cantidad del producto en el carrito

    def get_total_price(self):
        # Calcula el precio total de este item (cantidad * precio del producto)
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"

# Modelo para una Orden (cuando se finaliza un carrito)
class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Si decides implementar usuarios, una orden puede tener un usuario asociado.
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, blank=True)
    # Un carrito se convierte en una orden. OneToOne para evitar que un carrito sea parte de varias órdenes.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) # Cantidad total de la orden
    order_date = models.DateTimeField(auto_now_add=True) # Fecha de la orden (automático)
    status = models.CharField(max_length=50, default='Pending') # Estado de la orden (ej: Pendiente, Completado, Enviado)

    def __str__(self):
        return f"Order {self.id} - {self.status}"