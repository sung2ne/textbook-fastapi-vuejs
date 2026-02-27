<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const title = ref('')
const content = ref('')

function handleSubmit() {
  console.log('제출:', title.value, content.value)
  // PART 06에서 실제 API 호출로 교체합니다
  router.push('/')
}
</script>

<template>
  <h2>새 게시글</h2>
  <form @submit.prevent="handleSubmit">
    <div>
      <label>제목</label>
      <input v-model="title" />
    </div>
    <div>
      <label>내용</label>
      <textarea v-model="content"></textarea>
    </div>
    <button type="submit">등록</button>
  </form>
</template>
