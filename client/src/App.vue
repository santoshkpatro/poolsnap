<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  created() {
    const userString = localStorage.getItem('loggedInUser')

    if (userString) {
      const userData = JSON.parse(userString)
      this.$store.commit('SET_USER', userData)
    }

    axios.interceptors.response.use(
      (response) => response,
      (error) => {
        console.log(error.response)
        if (error.response.status === 401) {
          this.$router.push('/')
          this.$store.commit('removeLoginUser')
        }
        return Promise.reject(error)
      }
    )
  },
}
</script>

<style>
</style>
