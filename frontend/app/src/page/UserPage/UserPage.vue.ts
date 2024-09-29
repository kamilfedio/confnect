import { defineComponent, onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore'

export default defineComponent({
  name: 'UserPage',
  components: {},
  setup() {
    const userStore = useUserStore()

    onMounted(async () => {
      await userStore.fetchUser()
    })

    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      userStore
    }
  }
})
