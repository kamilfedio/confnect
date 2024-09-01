import { defineComponent } from 'vue'
import AuthBackground from '@/components/AuthBackground/AuthBackground.vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LandingPage',
  components: {
    AuthBackground
  },
  setup() {
    const router = useRouter()

    const goToLogin = () => {
      router.push('/login')
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      goToLogin
    }
  }
})
