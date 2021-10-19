import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue'),
    },
    {
        path: '/auth/login',
        name: 'Login',
        component: () => import('../views/auth/Login.vue'),
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('user')

    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!loggedIn) {
            next({
                path: '/auth/login',
                query: { redirect: to.fullPath },
            })
        } else {
            const isAdmin = JSON.parse(loggedIn).is_admin

            if (to.meta.requiresAdmin) {
                if (!isAdmin) {
                    next({
                        path: '/unauthorized',
                    })
                }
            }
            next()
        }
    } else {
        next()
    }
})

export default router
