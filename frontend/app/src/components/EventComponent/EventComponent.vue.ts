import { defineComponent } from 'vue'

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
    const formattedDate = () => {
      return props.event.date ? props.event.date.replace('T', ' ') : ''
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      formattedDate
    }
  }
})
