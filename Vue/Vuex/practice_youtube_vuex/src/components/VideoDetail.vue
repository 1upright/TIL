<template>
  <div v-if="newData[0]">
    <iframe :src="videoURI" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    newData: Array
  },
  computed: {
    videoURI() {
      const videoId = this.newData[2]
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>