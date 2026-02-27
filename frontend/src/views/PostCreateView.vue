<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import api from '@/api'

const router = useRouter()
const formRef = ref(null)
const isSubmitting = ref(false)

const form = reactive({
  title: '',
  content: '',
})

const rules = {
  title: [
    { required: true, message: '제목을 입력해주세요', trigger: 'blur' },
    { min: 2, max: 100, message: '2~100자로 입력해주세요', trigger: 'blur' },
  ],
  content: [
    { required: true, message: '내용을 입력해주세요', trigger: 'blur' },
  ],
}

async function handleSubmit() {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  isSubmitting.value = true
  try {
    await api.post('/posts', {
      title: form.title,
      content: form.content,
    })
    ElMessage.success('게시글이 작성되었습니다.')
    router.push('/')
  } catch (error) {
    ElMessage.error('게시글 작성에 실패했습니다.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div>
    <h2>새 게시글</h2>
    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-position="top"
    >
      <el-form-item label="제목" prop="title">
        <el-input v-model="form.title" maxlength="100" show-word-limit />
      </el-form-item>
      <el-form-item label="내용" prop="content">
        <el-input
          v-model="form.content"
          type="textarea"
          :rows="8"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          :loading="isSubmitting"
          @click="handleSubmit"
        >
          등록
        </el-button>
        <el-button @click="router.push('/')">취소</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
