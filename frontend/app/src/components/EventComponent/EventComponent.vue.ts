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
  setup() {
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {}
  }
})
