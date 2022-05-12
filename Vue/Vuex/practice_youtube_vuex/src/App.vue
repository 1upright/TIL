<template>
  <div id="app">
    <h1>Youtube Vuex Project</h1>
    <search-bar></search-bar>
    <video-detail :newData="newData"></video-detail>
    <video-list></video-list>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    SearchBar, VideoList, VideoDetail
  },
  computed: {
    ...mapState(['newData'])
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
