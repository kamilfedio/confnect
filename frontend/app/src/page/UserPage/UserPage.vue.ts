import { defineComponent, onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore'
import EventComponent from '@/components/EventComponent/EventComponent.vue'
import SearchPanel from '@/components/SearchPanel/SearchPanel.vue'
import AddEvent from '@/components/AddEvent/AddEvent.vue'

export default defineComponent({
  name: 'UserPage',
  components: {
    EventComponent,
    SearchPanel,
    AddEvent
  },
  setup() {
    const userStore = useUserStore()

    onMounted(() => {
      userStore.fetchUserEvents()
    })
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {}
  }
})
