import { defineComponent, ref, onMounted, onBeforeUnmount } from 'vue'
import LandingPageNavigation from '../../components/LandingPageNavigation/LandingPageNavigation.vue'
import FooterComponent from '@/components/FooterComponent/FooterComponent.vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LandingPage',
  components: {
    LandingPageNavigation,
    FooterComponent
  },
  setup() {
    // Reaktywne zmienne
    const userMessage = ref<string>('')
    const userName = ref<string>('')
    const userEmail = ref<string>('')
    const showScrollArrow = ref<boolean>(false)
    const messageError = ref<string>('')
    const emailError = ref<string>('')
    const nameError = ref<string>('')

    //Router
    const router = useRouter()

    const goToLogin = () => {
      router.push('/login')
    }

    const goToRegister = () => {
      router.push('/register')
    }

    // Funkcje do przewijania strony
    const scrollToFeatures = () => {
      const section = document.querySelector('.feature') as HTMLElement
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    }

    const scrollToAbout = () => {
      const section = document.querySelector('.journay') as HTMLElement
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    }

    const scrollToContact = () => {
      const section = document.querySelector('.writeToUs') as HTMLElement
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    }

    const scrollToTop = () => {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    const handleScroll = () => {
      showScrollArrow.value = window.scrollY > window.innerHeight
    }

    // Funkcje walidacji
    const validateEmail = () => {
      const atIndex = userEmail.value.indexOf('@')
      const dotAfterAt = userEmail.value.indexOf('.', atIndex)

      if (atIndex === -1 || dotAfterAt === -1) {
        emailError.value = 'Incorrect email format'
      } else {
        emailError.value = ''
      }
    }

    const validateMessage = () => {
      if (userMessage.value.length < 10) {
        messageError.value = 'The message must contain at least 10 characters'
      } else {
        messageError.value = ''
      }
    }

    const validateName = () => {
      if (userName.value.length < 3) {
        nameError.value = 'The name must contain at least 3 characters'
      } else {
        nameError.value = ''
      }
    }

    // Funkcja do wysyłania wiadomości
    const sendMessage = async () => {
      // Resetuj błędy
      messageError.value = ''
      emailError.value = ''
      nameError.value = ''

      // Walidacja danych
      validateEmail()
      validateMessage()
      validateName()

      if (messageError.value || emailError.value || nameError.value) {
        return
      }

      try {
        const response = await fetch('http://0.0.0.0:8000/api/v1/forms/', {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: userEmail.value,
            name: userName.value,
            content: userMessage.value
          })
        })

        const data = await response.json()

        // Resetowanie pól formularza po udanym wysłaniu
        userMessage.value = ''
        userName.value = ''
        userEmail.value = ''
      } catch (error) {
        console.error('Error:', error)
      }
    }

    // Lifecycle hooks
    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
      handleScroll()
    })

    onBeforeUnmount(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      userMessage,
      userName,
      userEmail,
      showScrollArrow,
      messageError,
      emailError,
      nameError,
      scrollToFeatures,
      scrollToAbout,
      scrollToContact,
      scrollToTop,
      sendMessage,
      goToLogin,
      goToRegister
    }
  }
})
