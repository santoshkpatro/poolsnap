<template>
  <div>
    <label :for="name" class="form-label">{{ clabel }}</label>
    <input
      :type="type"
      class="form-control"
      :name="name"
      :id="id"
      :required="required"
      :disabled="disabled"
      :value="value"
      @input="onChange($event.target.value)"
    />
    <div class="form-text" v-if="message">
      {{ message }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    value: {
      type: String,
      default: '',
    },
    id: {
      type: String,
    },
    label: {
      type: String,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    name: {
      type: String,
      required: true,
    },
    required: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
    },
    message: {
      type: String,
    },
    showRequired: {
      type: Boolean,
      default: false,
    },
    type: {
      type: String,
      default: 'text',
    },
  },
  emits: ['input'],
  computed: {
    clabel: function () {
      if (this.showRequired) {
        if (this.required) {
          return `${this.label} *`
        } else {
          return this.label
        }
      } else {
        return this.label
      }
    },
  },
  methods: {
    onChange(value) {
      this.$emit('input', value)
    },
  },
}
</script>

<style scoped>
input,
input:focus {
  background: transparent;
  outline: none;
  box-shadow: none;
}

input:focus {
  border-bottom: 3px solid var(--main);
}
</style>