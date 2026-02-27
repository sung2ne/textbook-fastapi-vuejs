<script setup>
import { ref } from 'vue'
import Timer from './components/Timer.vue'

const showTimer = ref(true)
</script>

<template>
  <button @click="showTimer = !showTimer">
    타이머 {{ showTimer ? '숨기기' : '보이기' }}
  </button>
  <Timer v-if="showTimer" />
</template>
