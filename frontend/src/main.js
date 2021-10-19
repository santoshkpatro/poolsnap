import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import { extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules'
import axios from 'axios'

Vue.config.productionTip = false

new Vue({
    router,
    store,
    vuetify,
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
