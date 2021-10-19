<template>
    <section class="hero is-fullheight">
        <div class="hero-body columns is-mobile is-centered">
            <div class="column is-one-third">
                <h1 class="title">Login</h1>
                <ValidationObserver v-slot="{ invalid }">
                    <form @submit.prevent="onSubmit" ref="loginForm">
                        <ValidationProvider
                            name="E-mail"
                            rules="required|email"
                            v-slot="{ errors }"
                        >
                            <b-field
                                label="Email"
                                :message="errors[0]"
                                :type="{
                                    'is-danger': errors[0],
                                    'is-primary': !errors,
                                }"
                            >
                                <b-input type="email" v-model="email">
                                </b-input>
                            </b-field>
                        </ValidationProvider>
                        <ValidationProvider
                            name="Password"
                            rules="required"
                            v-slot="{ errors }"
                        >
                            <b-field
                                label="Password"
                                :message="errors[0]"
                                :type="{
                                    'is-danger': errors[0],
                                    'is-primary': !errors,
                                }"
                            >
                                <b-input
                                    type="password"
                                    password-reveal
                                    v-model="password"
                                >
                                </b-input>
                            </b-field>
                        </ValidationProvider>
                        <b-button
                            class="my-5"
                            type="is-primary"
                            native-type="submit"
                            expanded
                            :disabled="invalid"
                            >Login</b-button
                        >
                    </form>
                </ValidationObserver>
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
                .then(({ data }) => {
                    this.$store.dispatch('login', data)
                    if (this.$route.query.redirect) {
                        this.$router.push(this.$route.query.redirect)
                    } else {
                        this.$router.push({ name: 'Home' })
                    }
                })
                .catch((e) => {
                    this.raiseNotification(e.response.data.detail, 'error')
                    this.$refs.loginForm.reset()
                })
        },
    },
}
</script>

<style>
</style>