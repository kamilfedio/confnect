import { defineComponent, onMounted, ref, watchEffect } from 'vue'
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
    const addEventDialogOpen = ref<boolean>(false)
    const eventListOpen = ref<boolean>(false)
    const twoEvents = ref<Array<Object>>([])

    const userStore = useUserStore()

    onMounted(async () => {
      await userStore.fetchUserEvents()
      console.log(userStore.events)
      if (userStore.events) {
        console.log(userStore.events.length)
        const max = userStore.events.length < 2 ? userStore.events.length : 2
        for (let i = 0; i < max; i++) {
          twoEvents.value.push(userStore.events[i])
        }
      }
    })

    watchEffect(() => {
      console.log('Events changed:', userStore.events)
    })

    const openAddEventDialog = () => {
      addEventDialogOpen.value = true
      console.log(addEventDialogOpen.value)
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
