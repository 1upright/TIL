<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model.trim='appInputData'>
    <p>parentData : {{ appParentData }}</p>
    <p>childData: {{ appChildData }}</p>
    <app-parent
    :app-data="appInputData"
    @parent-input="appGetParent"
    @child-input="appGetChild"
    >
    </app-parent>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data() {
    return {
      appInputData: '',
      appParentData: '',
      appChildData: ''
    }
  },
  methods: {
    appGetParent(parentData) {
      this.appParentData = parentData
    },
    appGetChild(childData) {
      this.appChildData = childData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
