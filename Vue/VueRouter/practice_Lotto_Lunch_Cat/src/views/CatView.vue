<template>
  <div>
    <h2>CAT</h2>
    <button @click='getCat'>Get Cat</button>
    <br>
    <img :src="`${ selectedCatUrl }`" alt="cat">
  </div>
</template>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import Axios from 'axios'

export default {
  name: 'CatView',
  data: function() {
    return {
      selectedCatUrl: '',
    }
  },
  methods: {
    getCat: function () {
      Axios.get('https://api.thecatapi.com/v1/images/search')
        .then(res => res.data[0].url)
        .then(url => {
          this.selectedCatUrl = url
          })
    },
  },
}
</script>

<style>

</style>