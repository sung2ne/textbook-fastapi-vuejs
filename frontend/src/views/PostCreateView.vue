<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api'

const router = useRouter()
const title = ref('')
const content = ref('')
const isSubmitting = ref(false)
const imageFile = ref(null)

function handleFileChange(event) {
  imageFile.value = event.target.files[0]
}

async function handleSubmit() {
  isSubmitting.value = true
  try {
    let imageUrl = null
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('file', imageFile.value)
      const uploadRes = await api.post('/upload/image', formData)
      imageUrl = uploadRes.data.url
    }

    await api.post('/posts', {
      title: title.value,
      content: content.value,
      image_url: imageUrl,
    })
    router.push('/')
  } catch (error) {
    console.error('작성 실패:', error)
    alert('게시글 작성에 실패했습니다.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <h2>새 게시글</h2>
  <form @submit.prevent="handleSubmit">
    <div>
      <label>제목</label>
      <input v-model="title" required minlength="2" maxlength="100" />
    </div>
    <div>
      <label>내용</label>
      <textarea v-model="content" required></textarea>
    </div>
    <div>
      <label>이미지</label>
      <input type="file" accept="image/*" @change="handleFileChange" />
    </div>
    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? '등록 중...' : '등록' }}
    </button>
  </form>
</template>
