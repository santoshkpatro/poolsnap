<template>
  <div class="container mt-3">
    <h1>Login</h1>
    <form @submit.prevent="handleSubmit">
      <BaseInput
        name="email"
        id="email"
        placeholder="Enter your email"
        label="Email Address"
        class="col-10 col-sm-8 col-md-4"
        :required="true"
        :showRequired="true"
        v-model="credentials.email"
      />
      <BaseInput
        name="password"
        id="password"
        placeholder="Enter your password"
        label="Password"
        class="col-10 col-sm-8 col-md-4"
        :required="true"
        :showRequired="true"
        v-model="credentials.password"
        type="password"
      />
      <BaseButton
        class="mt-3 col-10 col-sm-8 col-md-4"
        :extended="true"
        type="submit"
        value="Submit"
      />
    </form>
  </div>
</template>

<script>
import BaseInput from '@/components/base/BaseInput.vue'
import BaseButton from '@/components/base/BaseButton.vue'

export default {
  name: 'Login',
  components: {
    BaseInput,
    BaseButton,
  },
  data() {
    return {
      credentials: {
        email: '',
        password: '',
      },
    }
  },
  methods: {
    handleSubmit() {
      console.log(this.credentials)
    },
  },
}
</script>

<style>
</style>