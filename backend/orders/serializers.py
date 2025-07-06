from rest_framework import serializers
from .models import Cart, CartItem, Order
from products.models import Product # Asegúrate de importar Product para CartItemSerializer

# Serializador para los ítems individuales dentro de un carrito
class CartItemSerializer(serializers.ModelSerializer):
    # Muestra los detalles completos del producto dentro del item del carrito
    product = serializers.SerializerMethodField()
    # Campo para recibir el ID del producto al añadir/actualizar el item
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = CartItem
        # Incluye 'get_total_price' que es un método del modelo
        fields = ['id', 'product', 'product_id', 'quantity', 'get_total_price']
        read_only_fields = ['get_total_price'] # Este campo es calculado, no se envía

    def get_product(self, obj):
        # Obtiene el serializador de producto y lo devuelve
        # Importa ProductSerializer dentro de la función para evitar circular imports si products.models importa orders.models
        from products.serializers import ProductSerializer
        return ProductSerializer(obj.product).data

# Serializador para el Carrito completo
class CartSerializer(serializers.ModelSerializer):
    # Para incluir una lista de los CartItems asociados a este carrito
    items = CartItemSerializer(many=True, read_only=True)
    # Campos calculados para mostrar el total de ítems y el monto total del carrito
    total_items = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items', 'total_items', 'total_amount']

    def get_total_items(self, obj):
        return obj.items.count() # Cuenta cuántos ítems hay en el carrito

    def get_total_amount(self, obj):
        # Suma el precio total de todos los ítems en el carrito
        total = sum(item.get_total_price() for item in obj.items.all())
        return total

# Serializador para una Orden
class OrderSerializer(serializers.ModelSerializer):
    # Muestra los detalles completos del carrito asociado a esta orden
    cart_details = CartSerializer(source='cart', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'cart', 'total_amount', 'order_date', 'status', 'cart_details']
        # 'total_amount' y 'order_date' son calculados automáticamente o por el backend
        read_only_fields = ['order_date', 'status', 'total_amount']