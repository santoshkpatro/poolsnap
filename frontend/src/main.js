import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Buefy from 'buefy'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import { extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules'
import 'buefy/dist/buefy.css'

Vue.use(Buefy)
Vue.config.productionTip = false
Vue.mixin({
    methods: {
        raiseNotification(msg, type) {
            switch (type) {
                case 'success':
                    this.$buefy.notification.open({
                        type: 'is-success',
                        message: msg,
                    })
                    break

                case 'error':
                    this.$buefy.notification.open({
                        type: 'is-danger',
                        message: msg,
                    })
                    break

                default:
                    this.$buefy.notification.open(msg)
                    break
            }
        },
    },
})

new Vue({
    router,
    store,
    render: h => h(App),
    created() {
        const userString = localStorage.getItem('user')
        if (userString) {
            const userData = JSON.parse(userString)
            this.$store.commit('SET_USER', userData)
        }
        //
        axios.interceptors.response.use(
            response => response,
            error => {
                console.log(error.response)
                if (error.response.status === 401) {
                    this.$router.push('/')
                    this.$store.dispatch('logout')
                }
                return Promise.reject(error)
            }
        )
    },
}).$mount('#app')

extend('email', email)
extend('required', required)
Vue.component('ValidationProvider', ValidationProvider)
Vue.component('ValidationObserver', ValidationObserver)
