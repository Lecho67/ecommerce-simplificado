import React from 'react';
import ReactDOM from 'react-dom'; // CAMBIO: Importar ReactDOM directamente
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// CAMBIO: Usar ReactDOM.render en lugar de createRoot
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();