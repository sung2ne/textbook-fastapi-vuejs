<script setup>
import { ref } from 'vue'

const name = ref('')
</script>

<template>
  <h2>인사말 생성기</h2>
  <input v-model="name" placeholder="이름을 입력하세요" />
  <p v-if="name">안녕하세요, {{ name }}님!</p>
</template>
