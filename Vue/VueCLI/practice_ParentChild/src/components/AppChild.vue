<template>
  <div>
    <h1>AppChild</h1>
    <input type="text"
    @input="childInput"
    v-model.trim='appChildInputData'
    >
    <p>appdata: {{ appData }}</p>
    <p>parentData : {{ appParentData }}</p>
    <p>childData : {{ appChildInputData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appParentData: String,
    appData: String,
  },
  data() {
    return {
      appChildInputData: ''
    }
  },
  methods: {
    childInput() {
      this.$emit('child-input', this.appChildInputData)
    }
  }
}
</script>

<style>

</style>