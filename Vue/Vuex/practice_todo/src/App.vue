<template>
  <div id="app">
    <p> 전체 : {{ allTodosCount }}</p>
    <p> 완료 : {{ completedTodosCount }}</p>
    <p> 예정 : {{ uncompletedTodosCount }}</p>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList, TodoForm
  },
  computed: {
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount'
    ])
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
