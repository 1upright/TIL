<template>
  <div>
    <h2>로또 추첨기</h2>
    <h2>{{ $route.params.lottoNum }}개의 번호를 추천합니다</h2>
    <button @click='getLuckyNums'>Get Lucky Numbers</button>
    <p>추천 번호</p>
    <!-- <p>{{ selectedLuckyNums }}</p> -->
    <div v-for="number in selectedLuckyNums" :key="number" class="ball">{{ number }}</div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data: function() {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const nums = _.sampleSize(_.range(1, 46), this.$route.params.lottoNum,)
      nums.sort((a, b) => a - b)
      this.selectedLuckyNums = nums
    },
  },
}
</script>

<style>
  .ball {
    display: inline-block;
    width: 100px;
    height: 100px;
    line-height: 100px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    border-radius: 50px;
    background-color: gold;
  }
</style>