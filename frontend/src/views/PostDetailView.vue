<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const postId = route.params.id

const post = ref(null)

onMounted(() => {
  // PART 06에서 실제 API 호출로 교체합니다
  post.value = {
    id: postId,
    title: `${postId}번 게시글`,
    content: '게시글 내용입니다.',
  }
})

function goBack() {
  router.push('/')
}
</script>

<template>
  <div v-if="post">
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <button @click="goBack">목록으로</button>
  </div>
  <p v-else>로딩 중...</p>
</template>
