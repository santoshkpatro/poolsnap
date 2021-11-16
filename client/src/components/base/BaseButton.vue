<template>
  <div class="d-grid gap-2" v-if="extended">
    <button class="btn b-main" :id="id" :disabled="disabled" :type="type">
      {{ value }}
    </button>
  </div>
  <div v-else>
    <button class="btn b-main" :id="id" :disabled="disabled" :type="type">
      {{ value }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'BaseButton',
  props: {
    extended: {
      type: Boolean,
      default: false,
    },
    id: {
      type: String,
    },
    value: {
      type: String,
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    type: {
      type: String,
      default: 'button',
    },
  },
}
</script>

<style>
</style>