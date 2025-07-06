import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

// Importa las páginas
import HomePage from './pages/HomePage';
import ProductDetailPage from './pages/ProductDetailPage';
import CartPage from './pages/CartPage';

// Componente de página simple para el éxito de la orden
const OrderSuccessPage = () => (
    <div className="container mx-auto text-center mt-8 p-4 bg-green-100 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold text-green-700 mb-4">¡Gracias por tu compra!</h1>
        <p className="text-lg text-gray-700 mb-6">Tu pedido ha sido procesado con éxito.</p>
        <Link to="/" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300">
            Volver al inicio
        </Link>
    </div>
);

function App() {
    return (
        <Router>
            <nav className="bg-gray-800 p-4 shadow-md">
                <div className="container mx-auto flex justify-between items-center">
                    <Link className="text-white text-2xl font-bold hover:text-gray-300 transition duration-300" to="/">Mi E-commerce</Link>
                    <div className="space-x-4">
                        <Link className="text-gray-300 hover:text-white transition duration-300 px-3 py-2 rounded-md text-sm font-medium" to="/">Productos</Link>
                        <Link className="text-gray-300 hover:text-white transition duration-300 px-3 py-2 rounded-md text-sm font-medium" to="/cart">Carrito</Link>
                    </div>
                </div>
            </nav>
            {/* CAMBIO: De <Routes> a <Switch> y 'element' a 'component' */}
            <Switch>
                <Route exact path="/" component={HomePage} />
                <Route path="/product/:id" component={ProductDetailPage} />
                <Route path="/cart" component={CartPage} />
                <Route path="/order-success" component={OrderSuccessPage} />
            </Switch>
        </Router>
    );
}

export default App;