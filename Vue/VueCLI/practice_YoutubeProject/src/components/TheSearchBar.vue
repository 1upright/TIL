<template>
  <div>
    <input
      type="text"
      @keyup.enter="onInputKeyword"
      v-model="keyword"
    >
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      keyword: ''
    }
  },
  methods: {
    onInputKeyword: function () {
      this.$emit('input-change', this.keyword)
    }
  }
}
</script>

<style>

</style>