import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PostDetailView from '../views/PostDetailView.vue'
import PostCreateView from '../views/PostCreateView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/posts/new',
    name: 'post-create',
    component: PostCreateView,
  },
  {
    path: '/posts/:id',
    name: 'post-detail',
    component: PostDetailView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
