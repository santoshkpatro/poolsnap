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
            axios.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${userData.token}`
            state.user = userData
        },
    },
    actions: {
        login({ commit }, userData) {
            commit('SET_USER', userData)
        },
        // logout({ commit }) {
        //     commit('CLEAR_USER_DATA')
        // },
    },
    modules: {},
    getters: {
        loggedIn(state) {
            return !!state.user
        },
    },
})
