<template>
  <div id="app">
    <h1>Youtube Project</h1>
    <the-search-bar @input-change="onInputChange"></the-search-bar>
    <video-detail :video="selectedVideo"></video-detail>
    <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

const API_KEY = 
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange: function (inputText) {
      this.inputValue = inputText

      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue
        }
      })
        .then(res => {
          this.videos = res.data.items
        })
        .catch(error => {
          console.log(error)
        })
    },

    onVideoSelect: function(video) {
      this.selectedVideo = video
    }
  },
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
