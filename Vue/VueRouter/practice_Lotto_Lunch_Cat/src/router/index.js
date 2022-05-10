import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LottoView from '../views/LottoView.vue'
import LunchView from '../views/LunchView.vue'
import CatView from '../views/CatView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/lotto',
    name: 'lotto',
    component: LottoView
  },
  {
    path: '/lunch',
    name: 'lunch',
    component: LunchView
  },
  {
    path: '/cat',
    name: 'cat',
    component: CatView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
