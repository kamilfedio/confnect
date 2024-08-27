import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/page/LandingPage/LandingPage.vue'
import LoginPage from '@/page/LoginPage/LoginPage.vue'
import RegisterPage from '@/page/RegisterPage/RegisterPage.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
