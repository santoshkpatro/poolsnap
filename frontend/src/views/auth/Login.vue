<template>
    <section class="hero is-fullheight">
        <div class="hero-body columns is-mobile is-centered">
            <div class="column is-one-third">
                <form @submit.prevent="onSubmit">
                    <b-field label="Email">
                        <b-input type="email" v-model="email"> </b-input>
                    </b-field>
                    <b-field label="Password">
                        <b-input
                            type="password"
                            password-reveal
                            v-model="password"
                        >
                        </b-input>
                    </b-field>
                    <b-button type="is-primary" native-type="submit" expanded
                        >Login</b-button
                    >
                </form>
            </div>
        </div>
    </section>
</template>

<script>
import { login } from '@/api'

export default {
    name: 'Login',
    data() {
        return {
            email: null,
            password: null,
        }
    },
    methods: {
        onSubmit() {
            const credentials = {
                email: this.email,
                password: this.password,
            }
            login(credentials)
                .then(({ data }) => this.$store.dispatch('login', data))
                .catch((e) => console.log(e))
        },
    },
}
</script>

<style>
</style>