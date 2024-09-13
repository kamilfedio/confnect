import { defineComponent, ref } from 'vue'
import AuthBackground from '@/components/AuthBackground/AuthBackground.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'

export default defineComponent({
  name: 'LandingPage',
  components: {
    AuthBackground
  },
  setup() {
    // Reaktywne zmienne
    const email = ref<string>('')
    const name = ref<string>('')
    const password = ref<string>('')
    const acceptRules = ref<boolean>(false)

    const nameError = ref<string>('')
    const emailError = ref<string>('')
    const passwordError = ref<string>('')
    const rulesError = ref<string>('')

    const router = useRouter()
    const userStore = useUserStore()

    const goToLogin = () => {
      router.push('/login')
    }

    const submitForm = async () => {
      try {
        const response = await fetch('http://0.0.0.0:8000/register', {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: email.value,
            name: name.value,
            password: password.value
          })
        })

        if (!response.ok) {
          let errorMessage = 'Unknown error occurred.'

          if (response.status === 400) {
            emailError.value = 'The email address is already used'
          } else if (response.status === 401) {
            errorMessage = 'Unauthorized. Please try again.'
          } else if (response.status === 500) {
            errorMessage = 'Server error. Please try again later.'
          }

          throw alert(errorMessage)
        }

        const data = await response.json()

        const { access_token, refresh_token } = data

        if (access_token && refresh_token) {
          userStore.setAccessToken(access_token)
          document.cookie = `refreshToken=${refresh_token}; path=/; max-age=604800; secure; SameSite=Strict`

          router.push({ name: 'UserPage' })
        } else {
          throw new Error('Missing tokens in response')
        }
      } catch (error) {
        console.error('Error during registration:', error)
      }
    }
    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      email,
      name,
      password,
      acceptRules,
      emailError,
      nameError,
      passwordError,
      rulesError,
      goToLogin,
      submitForm
    }
  }
})
