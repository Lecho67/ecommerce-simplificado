import React, { useEffect, useState } from 'react';
import { useParams, useHistory } from 'react-router-dom'; // CAMBIO: 'useNavigate' a 'useHistory'
import api from '../api/api';

function ProductDetailPage() {
    const { id } = useParams();
    const history = useHistory(); // CAMBIO: de 'navigate' a 'history'
    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [quantity, setQuantity] = useState(1);
    const [cartId, setCartId] = useState(localStorage.getItem('cartId'));

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await api.get(`/products/${id}/`);
                setProduct(response.data);
            } catch (err) {
                setError('Producto no encontrado.');
                console.error('Error fetching product:', err);
            } finally {
                setLoading(false);
            }
        };
        fetchProduct();
    }, [id]);

    const handleAddToCart = async () => {
        let currentCartId = cartId;
        if (!currentCartId) {
            try {
                const response = await api.get('/carts/current/');
                currentCartId = response.data.id;
                localStorage.setItem('cartId', currentCartId);
                setCartId(currentCartId);
            } catch (err) {
                alert('Error al obtener/crear el carrito.');
                console.error('Error fetching/creating cart:', err);
                return;
            }
        }

        try {
            await api.post(`/carts/${currentCartId}/add_item/`, {
                product_id: product.id,
                quantity: quantity,
            });
            alert('Producto añadido al carrito!');
            history.push('/cart'); // CAMBIO: de 'navigate('/cart')' a 'history.push('/cart')'
        } catch (err) {
            alert('Error al añadir producto al carrito.');
            console.error('Error adding to cart:', err.response ? err.response.data : err);
        }
    };

    if (loading) return <div className="text-center mt-8 text-xl text-gray-600">Cargando producto...</div>;
    if (error) return <div className="text-center mt-8 text-xl text-red-600">{error}</div>;
    if (!product) return null;

    return (
        <div className="container mx-auto px-4 py-8">
            <div className="flex flex-col md:flex-row gap-8 items-center">
                <div className="md:w-1/2">
                    <img src={product.image_url || 'https://via.placeholder.com/400'} className="w-full h-auto rounded-lg shadow-lg" alt={product.name} />
                </div>
                <div className="md:w-1/2 p-4">
                    <h1 className="text-4xl font-bold text-gray-900 mb-2">{product.name}</h1>
                    <p className="text-lg text-gray-600 mb-4">{product.category_name}</p>
                    <p className="text-3xl font-semibold text-blue-700 mb-4">${product.price}</p>
                    <p className="text-gray-700 mb-6">{product.description}</p>
                    <div className="mb-6">
                        <label htmlFor="quantity" className="block text-gray-700 text-sm font-bold mb-2">Cantidad:</label>
                        <input
                            type="number"
                            id="quantity"
                            className="shadow appearance-none border rounded w-24 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            value={quantity}
                            onChange={(e) => setQuantity(Math.max(1, parseInt(e.target.value) || 1))}
                            min="1"
                        />
                    </div>
                    <button className="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-lg shadow-md transition duration-300" onClick={handleAddToCart}>
                        Añadir al Carrito
                    </button>
                </div>
            </div>
        </div>
    );
}

export default ProductDetailPage;