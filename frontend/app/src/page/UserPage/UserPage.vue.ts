import { defineComponent } from 'vue'
import EventComponent from '@/components/EventComponent/EventComponent.vue'

export default defineComponent({
  name: 'UserPage',
  components: {
    EventComponent
  },
  setup() {
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {}
  }
})
