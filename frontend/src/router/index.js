import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PostDetailView from '../views/PostDetailView.vue'
import PostCreateView from '../views/PostCreateView.vue'
import PostEditView from '../views/PostEditView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/posts/new', name: 'post-create', component: PostCreateView },
  { path: '/posts/:id/edit', name: 'post-edit', component: PostEditView },
  { path: '/posts/:id', name: 'post-detail', component: PostDetailView },
  { path: '/login', name: 'login', component: LoginView },
  { path: '/signup', name: 'signup', component: SignupView },
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
