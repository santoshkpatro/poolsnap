import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    loggedInUser: null,
    itemCart: [],
  },
  mutations: {
    setLoginUser(state, userData) {
      axios.defaults.headers.common[
        'Authorization'
      ] = `Bearer ${userData.token}`
      localStorage.setItem('loggedInUser', JSON.stringify(userData))
      state.loggedInUser = userData
    },

    removeLoginUser(state) {
      localStorage.removeItem('loggedInUser')
      state.loggedInUser = null
      location.reload()
    },

    addItemToCart(state, item) {
      state.itemCart.push(item)
    },

    removeItemFromCart(state, itemId) {
      state.itemCart = state.itemCart.filter((item) => item.id != itemId)
    },

    emptyCart(state) {
      state.itemCart = []
    },
  },
  actions: {},
  modules: {},
  getters: {
    isLoggedIn(state) {
      return !!state.loggedInUser
    },
    isAdmin(state) {
      return state.loggedInUser.is_admin
    },
  },
})
