import { defineComponent, ref, onMounted, onBeforeUnmount } from 'vue'
import AuthBackground from '@/components/AuthBackground/AuthBackground.vue'

export default defineComponent({
  name: 'LandingPage',
  components: {
    AuthBackground
  },
  setup() {
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {}
  }
})
