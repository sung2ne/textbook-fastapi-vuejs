<script setup>
import { ref } from 'vue'

const newTodo = ref('')
const todos = ref([])

function addTodo() {
  if (newTodo.value.trim()) {
    todos.value.push(newTodo.value)
    newTodo.value = ''
  }
}

function removeTodo(index) {
  todos.value.splice(index, 1)
}
</script>

<template>
  <h2>할 일 목록</h2>
  <form @submit.prevent="addTodo">
    <input v-model="newTodo" placeholder="할 일 입력" />
    <button type="submit">추가</button>
  </form>
  <ul>
    <li v-for="(todo, i) in todos" :key="i">
      {{ todo }}
      <button @click="removeTodo(i)">삭제</button>
    </li>
  </ul>
</template>
