import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_KEY = 
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    newDatas : [],
    newData : []
  },
  getters: {
  },
  mutations: {
    GET_TITLE_URL(state, newDatas) {
      state.newDatas = newDatas
    },
    GET_SINGLE_DATA(state, newData) {
      state.newData = newData
    }
  },
  actions: {
    inputKeyword({ commit }, keyword) {
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: keyword
        }
      })
        .then(res => {
          const datas = res.data.items
          const newDatas = datas.map(x => [x.snippet.title, x.snippet.thumbnails.default.url, x.id.videoId])
          commit('GET_TITLE_URL', newDatas)
        })
    },
    selectVideo({ commit }, newData) {
      commit('GET_SINGLE_DATA', newData)
    }
  },
  modules: {
  }
})
