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

    const goToRegister = () => {
      router.push('/register')
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      goToRegister
    }
  }
})
