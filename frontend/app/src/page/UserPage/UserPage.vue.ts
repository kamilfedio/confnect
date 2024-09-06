import { defineComponent } from 'vue'
import EventComponent from '@/components/EventComponent/EventComponent.vue'
import SearchPanel from '@/components/SearchPanel/SearchPanel.vue'

export default defineComponent({
  name: 'UserPage',
  components: {
    EventComponent,
    SearchPanel
  },
  setup() {
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {}
  }
})
