import axios from 'axios'

const http = axios.create({
    baseURL: process.env.VUE_APP_ROOT_URL || '/',
})

export const login = data => http.post('/api/auth/login/', data)
