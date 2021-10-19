<template>
    <b-navbar id="nav">
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <p>Poolsnap</p>
            </b-navbar-item>
        </template>
        <template #start> </template>

        <template #end>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <router-link
                        class="button is-primary"
                        v-if="!loggedIn"
                        :to="{ name: 'Register' }"
                    >
                        <strong>Sign up</strong>
                    </router-link>
                    <router-link
                        class="button is-light"
                        v-if="!loggedIn"
                        :to="{ name: 'Login' }"
                    >
                        Log in
                    </router-link>
                    <router-link
                        :to="{ name: 'Overview' }"
                        class="button is-light"
                        v-if="isAdmin"
                        >Admin Panel</router-link
                    >
                    <button
                        class="button is-primary"
                        v-if="loggedIn"
                        @click="handleLogout"
                    >
                        Logout
                    </button>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Nav',
    computed: {
        ...mapGetters(['loggedIn', 'isAdmin']),
    },
    methods: {
        handleLogout() {
            this.$store.dispatch('logout')
        },
    },
}
</script>

<style scoped>
</style>