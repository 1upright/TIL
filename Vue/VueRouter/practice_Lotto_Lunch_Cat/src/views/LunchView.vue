<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click='getLunchMenu'>Pick Lunch</button>
    <p>{{ selectedMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data: function () {
    return {
      selectedMenu: '',
    }
  },
  methods: {
    getLunchMenu: function () {
      this.selectedMenu = _.sample(['국밥', '자장면', '제육볶음'])
    },
  },
}
</script>

<style>

</style>