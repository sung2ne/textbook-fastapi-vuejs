<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import PostCard from '@/components/PostCard.vue'

const posts = ref([])
const isLoading = ref(true)

onMounted(async () => {
  try {
    const response = await api.get('/posts')
    posts.value = response.data
  } catch (error) {
    console.error('목록 로드 실패:', error)
  } finally {
    isLoading.value = false
  }
})

async function handleDelete(postId) {
  if (confirm('정말 삭제하시겠습니까?')) {
    await api.delete(`/posts/${postId}`)
    posts.value = posts.value.filter(p => p.id !== postId)
  }
}
</script>

<template>
  <h2>게시판</h2>
  <p v-if="isLoading">로딩 중...</p>
  <div v-else>
    <PostCard
      v-for="post in posts"
      :key="post.id"
      :post="post"
      @delete="handleDelete"
    />
  </div>
  <p v-if="!isLoading && posts.length === 0">
    아직 게시글이 없습니다.
  </p>
  <RouterLink to="/posts/new">새 글 작성</RouterLink>
</template>
