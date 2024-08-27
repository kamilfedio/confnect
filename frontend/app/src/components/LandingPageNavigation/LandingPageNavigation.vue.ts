import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LandingPageNavigation',
  props: {
    onScrollToFeatures: {
      type: Function,
      required: true
    },
    onScrollToAbout: {
      type: Function,
      required: true
    },
    onScrollToContact: {
      type: Function,
      required: true
    }
  }
})
