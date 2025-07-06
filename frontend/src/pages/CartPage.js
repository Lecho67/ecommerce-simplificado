import React, { useEffect, useState } from 'react';
import api from '../api/api';
import { useHistory } from 'react-router-dom'; // CAMBIO: 'useNavigate' a 'useHistory'

function CartPage() {
    const [cart, setCart] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const history = useHistory(); // CAMBIO: de 'navigate' a 'history'
    const cartId = localStorage.getItem('cartId');

    useEffect(() => {
        const fetchCart = async () => {
            if (!cartId) {
                setLoading(false);
                return;
            }
            try {
                const response = await api.get(`/carts/${cartId}/`);
                setCart(response.data);
            } catch (err) {
                setError('Error al cargar el carrito. Asegúrate de que el ID del carrito es válido o que tienes un carrito.');
                console.error('Error fetching cart:', err);
                localStorage.removeItem('cartId');
            } finally {
                setLoading(false);
            }
        };
        fetchCart();
    }, [cartId]);

    const handleUpdateQuantity = async (productId, newQuantity) => {
        if (newQuantity <= 0) {
            handleRemoveItem(productId);
            return;
        }
        try {
            const response = await api.post(`/carts/${cartId}/update_item_quantity/`, {
                product_id: productId,
                quantity: newQuantity,
            });
            setCart(response.data);
        } catch (err) {
            alert('Error al actualizar la cantidad.');
            console.error('Error updating quantity:', err.response ? err.response.data : err);
        }
    };

    const handleRemoveItem = async (productId) => {
        try {
            const response = await api.post(`/carts/${cartId}/remove_item/`, {
                product_id: productId,
            });
            setCart(response.data);
        } catch (err) {
            alert('Error al eliminar el producto.');
            console.error('Error removing item:', err.response ? err.response.data : err);
        }
    };

    const handleCheckout = async () => {
        if (!cart || !cart.items || cart.items.length === 0) {
            alert('El carrito está vacío.');
            return;
        }
        try {
            const response = await api.post('/orders/create_order_from_cart/', {
                cart_id: cart.id,
            });
            alert(`Pedido creado! ID: ${response.data.id}. Total: $${cart.total_amount.toFixed(2)}`);
            localStorage.removeItem('cartId');
            setCart(null);
            history.push('/order-success'); // CAMBIO: de 'navigate('/order-success')' a 'history.push('/order-success')'
        } catch (err) {
            alert('Error al procesar el pedido.');
            console.error('Error creating order:', err.response ? err.response.data : err);
        }
    };

    if (loading) return <div className="text-center mt-8 text-xl text-gray-600">Cargando carrito...</div>;
    if (error) return <div className="text-center mt-8 text-xl text-red-600">{error}</div>;

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold text-gray-800 mb-8 text-center">Tu Carrito de Compras</h1>
            {!cart || cart.items.length === 0 ? (
                <div className="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative text-center" role="alert">
                    Tu carrito está vacío. <a href="/" className="text-blue-800 hover:underline font-semibold">Explora productos</a>
                </div>
            ) : (
                <>
                    <ul className="bg-white shadow-md rounded-lg mb-8">
                        {cart.items.map(item => (
                            <li key={item.id} className="flex justify-between items-center p-6 border-b border-gray-200 last:border-b-0">
                                <div className="flex-grow">
                                    <h5 className="text-xl font-semibold text-gray-900">{item.product.name}</h5>
                                    <p className="text-gray-600">${item.product.price} x {item.quantity}</p>
                                </div>
                                <div className="flex items-center space-x-4">
                                    <input
                                        type="number"
                                        value={item.quantity}
                                        onChange={(e) => handleUpdateQuantity(item.product.id, parseInt(e.target.value) || 0)}
                                        min="0"
                                        className="w-20 text-center border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                    <button className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-md transition duration-300" onClick={() => handleRemoveItem(item.product.id)}>
                                        Eliminar
                                    </button>
                                </div>
                            </li>
                        ))}
                    </ul>
                    <div className="flex justify-end items-center mt-8 p-6 bg-white shadow-lg rounded-lg">
                        <h3 className="text-3xl font-bold text-gray-900 mr-6">Total: ${cart.total_amount.toFixed(2)}</h3>
                        <button className="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-lg shadow-md transition duration-300" onClick={handleCheckout}>
                            Finalizar Compra
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}

export default CartPage;