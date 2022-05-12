<template>
  <input
  @keyup.enter="inputKeyword"
  v-model.trim="keyword"
  type="text"
  >
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: ''
    }
  },
  methods: {
    inputKeyword() {
      this.$store.dispatch('inputKeyword', this.keyword)
      this.keyword = ''
    }
  }
}
</script>

<style>

</style>