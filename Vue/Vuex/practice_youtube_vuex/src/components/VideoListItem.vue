<template>
  <li @click="selectVideo">
    <img :src="newData[1]" alt="thumbnail">
    {{ newData[0] }}
  </li>
</template>

<script>

export default {
  name: 'VideoListItem',
  props: {
    newData: Array
  },
  methods: {
    selectVideo() {
      this.$store.dispatch('selectVideo', this.newData)
    }
  }
}
</script>

<style>

</style>