import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: null,
    },
    mutations: {
        SET_USER(state, userData) {
            localStorage.setItem('user', JSON.stringify(userData))
            axios.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${userData.token}`
            state.user = userData
        },
        CLEAR_USER(state) {
            localStorage.removeItem('user')
            state.user = null
            location.reload()
        },
    },
    actions: {
        login({ commit }, userData) {
            commit('SET_USER', userData)
        },
        logout({ commit }) {
            commit('CLEAR_USER')
        },
    },
    modules: {},
    getters: {
        loggedIn(state) {
            return !!state.user
        },
        isAdmin(state) {
            if (state.user) {
                return state.user.is_admin
            } else {
                return false
            }
        },
    },
})
