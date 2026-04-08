import axios from 'axios';

const api = axios.create({
    // Django domyślnie działa na porcie 8000
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    },
});

// W przyszłości dodamy tu interceptory dla tokenów JWT (logowanie)

export default api;