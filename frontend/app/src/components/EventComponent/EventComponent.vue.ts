import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'EventComponent',
  components: {},
  props: {
    event: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const router = useRouter()

    const formattedDate = () => {
      return props.event.date ? props.event.date.replace('T', ' ') : ''
    }

    const goToEventDetails = () => {
      router.push({ name: 'EventDetails', params: { id: props.event.id } })
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      formattedDate,
      goToEventDetails
    }
  }
})
