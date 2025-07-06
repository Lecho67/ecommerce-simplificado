import React from 'react';
import { Link } from 'react-router-dom';

function ProductCard({ product }) {
    return (
        <div className="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col h-full">
            <img src={product.image_url || 'https://via.placeholder.com/150'} className="w-full h-48 object-cover" alt={product.name} />
            <div className="p-6 flex flex-col flex-grow">
                <h5 className="text-xl font-bold text-gray-900 mb-2">{product.name}</h5>
                <p className="text-gray-600 text-sm mb-4">{product.category_name}</p>
                <p className="text-gray-700 text-base mb-4 flex-grow">{product.description.substring(0, 100)}...</p>
                <div className="flex justify-between items-center mt-auto">
                    <span className="text-2xl font-semibold text-blue-700">${product.price}</span>
                    <Link to={`/product/${product.id}`} className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                        Ver Detalles
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default ProductCard;