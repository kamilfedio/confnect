import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/page/LandingPage/LandingPage.vue'
import LoginPage from '@/page/LoginPage/LoginPage.vue'
import RegisterPage from '@/page/RegisterPage/RegisterPage.vue'
import UserPage from '@/page/UserPage/UserPage.vue'
import MainPage from '@/page/MainPage/MainPage.vue'
import EventDetailsPage from '@/page/EventDetailsPage/EventDetailsPage.vue'
import { isAuthenticated } from '../utils/auth.js'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage,
    meta: { requiresGuest: true }
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage,
    meta: { requiresGuest: true }
  },
  {
    path: '/confnect',
    name: 'UserPage',
    component: UserPage,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'MainPage',
        component: MainPage
      },
      {
        path: ':id',
        name: 'EventDetails',
        component: EventDetailsPage,
        props: true
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  // Jeśli uźytkownik jest zalogowany
  if (to.matched.some((record) => record.meta.requiresGuest)) {
    if (isAuthenticated()) {
      next({ name: 'UserPage' })
    } else {
      next()
    }
  }
  // Jeśli strona wymaga zalogowania
  else if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      next({ name: 'LoginPage' })
    } else {
      if (to.name === 'UserPage' && to.path === '/confnect') {
        next({ name: 'MainPage' })
      } else {
        next()
      }
    }
  } else {
    next()
  }
})

export default router
