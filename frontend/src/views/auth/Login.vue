<template>
    <div class="container">
        <h1>Login</h1>
        <ValidationObserver ref="observer" v-slot="{ invalid }">
            <form @submit.prevent="submit">
                <ValidationProvider
                    v-slot="{ errors }"
                    name="email"
                    rules="required|email"
                >
                    <v-text-field
                        v-model="email"
                        :error-messages="errors"
                        label="E-mail"
                        required
                    ></v-text-field>
                </ValidationProvider>
                <ValidationProvider
                    v-slot="{ errors }"
                    name="password"
                    rules="required"
                >
                    <v-text-field
                        v-model="password"
                        :error-messages="errors"
                        label="Password"
                        type="password"
                        required
                    ></v-text-field>
                </ValidationProvider>
                <v-btn class="mr-4" type="submit" :disabled="invalid" block>
                    submit
                </v-btn>
                <!-- <v-btn @click="clear" block> clear </v-btn> -->
            </form>
        </ValidationObserver>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        submit() {
            this.$refs.observer.validate()
        },
        clear() {
            this.name = ''
            this.password = ''
            this.$refs.observer.reset()
        },
    },
}
</script>

<style>
</style>