<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const messages = ref([])
const newMessage = ref('')
const chatBox = ref(null)
let ws = null
let reconnectTimer = null
const isConnected = ref(false)

const wsUrl = (import.meta.env.VITE_API_URL || 'http://localhost:8000')
  .replace('http', 'ws') + '/ws/chat'
</script>
