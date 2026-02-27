<script setup>
const name = '홍길동'
const role = '풀스택 개발자'
</script>

<template>
  <div class="card">
    <h2>{{ name }}</h2>
    <p>{{ role }}</p>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  max-width: 300px;
  text-align: center;
}

h2 {
  margin: 0 0 8px;
  color: #2c3e50;
}

p {
  margin: 0;
  color: #666;
}
</style>
