import axios from 'axios';
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/';
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});
export default api;