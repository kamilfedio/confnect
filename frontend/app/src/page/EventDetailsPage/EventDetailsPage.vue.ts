import { defineComponent, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { refreshAccessToken } from '../../utils/auth.js'

export default defineComponent({
  name: 'EventDetailsPage',
  components: {},
  setup() {
    const event = ref<Object>({})

    const route = useRoute()
    const id = route.params.id

    onMounted(async () => {
      try {
        let response = await fetch(`http://0.0.0.0:8000/api/v1/events/${id}`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            'Content-Type': 'application/json'
          }
        })

        if (response.status === 401) {
          await refreshAccessToken()
          response = await fetch(`http://0.0.0.0:8000/api/v1/events/${id}`, {
            method: 'GET',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
              'Content-Type': 'application/json'
            }
          })
        }
        if (!response.ok) {
          throw new Error('Failed to fetch event')
        }

        const data = await response.json()
        event.value = data
        console.log(event.value)
      } catch (error) {
        console.error('Error fetching event:', error)
        throw error
      }
      // const event = userStore.events.find(event => event.id === id)
    })
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      event
    }
  }
})
