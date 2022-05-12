<template>
  <div>
    <h1>AppParent</h1>
    <input type="text"
    @input="parentInput"
    v-model.trim="appParentInputData"
    >
    <p>appData : {{ appData }}</p>
    <p>childData : {{ appChildData }}</p>
    <app-child
    :app-parent-data="appParentInputData"
    :app-data="appData"
    @child-input="parentGetChild"
    >
    </app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    appData: String,
  },
  data() {
    return {
      appParentInputData: '',
      appChildData: '',
    }
  },
  methods: {
    parentGetChild(parentData) {
      this.appChildData = parentData
      this.$emit('child-input', this.appChildData)
    },
    parentInput() {
      this.$emit('parent-input', this.appParentInputData)
    },
  }
}
</script>

<style>

</style>