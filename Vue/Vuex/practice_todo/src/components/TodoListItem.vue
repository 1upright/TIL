<template>
  <div>
    <span
    @click="updateTodoStatus(todo)"
    :class="{ 'is_completed': todo.isCompleted }"
    >
    {{ todo.title }}</span>
    <button @click="deleteTodo(todo)">X</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodoStatus'])
  }
}
</script>

<style>
  .is_completed {
    text-decoration: line-through;
  }
</style>