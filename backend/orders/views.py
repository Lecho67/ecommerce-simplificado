from rest_framework import viewsets, status
from rest_framework.decorators import action # Para acciones personalizadas
from rest_framework.response import Response # Para devolver respuestas HTTP
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from products.models import Product # Necesitamos el modelo Product para añadir items al carrito

# ViewSet para los Carritos
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Acción personalizada para obtener el carrito actual (simplificado para desarrollo)
    # Esto es un endpoint GET /api/carts/current/
    @action(detail=False, methods=['get'])
    def current(self, request):
        # Lógica simplificada: siempre obtenemos/creamos un carrito con ID=1.
        # En una aplicación real, esto se manejaría con sesiones, cookies, o autenticación de usuario.
        cart, created = Cart.objects.get_or_create(id=1)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    # Acción personalizada para añadir un producto al carrito
    # Esto es un endpoint POST /api/carts/{id}/add_item/
    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object() # Obtiene el carrito por su ID (pk)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1) # Cantidad por defecto 1

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Intenta obtener el CartItem existente o crea uno nuevo
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity} # Si se crea, usa esta cantidad inicial
        )
        if not created:
            # Si ya existe, incrementa la cantidad
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.get_serializer(cart) # Devuelve el carrito actualizado
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Acción personalizada para eliminar un producto del carrito
    # Esto es un endpoint POST /api/carts/{id}/remove_item/
    @action(detail=True, methods=['post'])
    def remove_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')

        try:
            cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
            cart_item.delete() # Elimina el item del carrito
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Acción personalizada para actualizar la cantidad de un item en el carrito
    # Esto es un endpoint POST /api/carts/{id}/update_item_quantity/
    @action(detail=True, methods=['post'])
    def update_item_quantity(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        new_quantity = request.data.get('quantity')

        # Validar que la nueva cantidad sea un número positivo
        if new_quantity is None or not isinstance(new_quantity, int) or new_quantity < 0:
            return Response({'error': 'Quantity must be a non-negative integer'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
            if new_quantity == 0:
                cart_item.delete() # Si la cantidad es 0, se elimina el item
            else:
                cart_item.quantity = new_quantity
                cart_item.save()
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ViewSet para las Órdenes
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Acción personalizada para crear una orden a partir de un carrito
    # Esto es un endpoint POST /api/orders/create_order_from_cart/
    @action(detail=False, methods=['post'])
    def create_order_from_cart(self, request):
        cart_id = request.data.get('cart_id')

        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        if not cart.items.exists():
            return Response({'error': 'Cannot create order from an empty cart'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = sum(item.get_total_price() for item in cart.items.all())

        # Aquí podrías añadir lógica más compleja:
        # - Asociar la orden a un usuario autenticado (si implementas autenticación)
        # - Añadir dirección de envío, método de pago, etc.
        # - Reducir el stock de los productos.

        order = Order.objects.create(
            cart=cart,
            total_amount=total_amount,
            status='Pending' # Estado inicial de la orden
        )

        # Opcional: Vaciar el carrito después de crear la orden
        # cart.items.all().delete()
        # cart.delete() # También podrías borrar el carrito si es de un solo uso por orden

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)