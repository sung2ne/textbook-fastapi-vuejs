<script setup>
import BaseLayout from './components/BaseLayout.vue'
</script>

<template>
  <BaseLayout>
    <template #header>
      <h1>FastAPI + Vue 게시판</h1>
      <nav>
        <RouterLink to="/">홈</RouterLink>
        <RouterLink to="/posts/new">새 글 작성</RouterLink>
      </nav>
    </template>

    <RouterView />
  </BaseLayout>
</template>
