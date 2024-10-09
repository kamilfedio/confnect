import { defineComponent, onMounted, ref, watchEffect } from 'vue'
import { useUserStore, type UserEvent } from '@/stores/userStore'
import EventComponent from '@/components/EventComponent/EventComponent.vue'
import SearchPanel from '@/components/SearchPanel/SearchPanel.vue'
import AddEvent from '@/components/AddEvent/AddEvent.vue'

export default defineComponent({
  name: 'MainPage',
  components: {
    EventComponent,
    SearchPanel,
    AddEvent
  },
  setup() {
    const addEventDialogOpen = ref<boolean>(false)
    const eventListOpen = ref<boolean>(false)
    const twoEvents = ref<Array<UserEvent>>([])

    const userStore = useUserStore()

    onMounted(async () => {
      await userStore.fetchUserEvents()
    })

    watchEffect(() => {
      console.log('Events changed:', userStore.events)
      if (userStore.events) {
        const max = userStore.events.length < 2 ? userStore.events.length : 2
        for (let i = 0; i < max; i++) {
          twoEvents.value.push(userStore.events[i])
        }
      }
    })

    const openAddEventDialog = () => {
      addEventDialogOpen.value = true
    }

    const closeAddEventDialog = () => {
      addEventDialogOpen.value = false
    }

    const openAllEvents = () => {
      eventListOpen.value = true
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      userStore,
      addEventDialogOpen,
      eventListOpen,
      twoEvents,
      openAddEventDialog,
      closeAddEventDialog,
      openAllEvents
    }
  }
})
