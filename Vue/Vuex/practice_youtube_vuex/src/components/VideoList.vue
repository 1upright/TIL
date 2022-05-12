<template>
  <ul>
    <video-list-item
    v-for="(newData, idx) in newDatas"
    :key="idx"
    :newData="newData"
    >
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
import { mapState } from 'vuex'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  computed: {
    ...mapState(['newDatas'])
  },
}
</script>

<style>

</style>