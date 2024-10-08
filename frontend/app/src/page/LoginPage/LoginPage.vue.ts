import { defineComponent, ref } from 'vue'
import AuthBackground from '@/components/AuthBackground/AuthBackground.vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LandingPage',
  components: {
    AuthBackground
  },
  setup() {
    // Reaktywne zmienne
    const email = ref<string>('')
    const password = ref<string>('')

    const router = useRouter()

    const goToRegister = () => {
      router.push('/register')
    }

    const submitForm = () => {
      const formData = new URLSearchParams()
      formData.append('username', email.value)
      formData.append('password', password.value)
      formData.append('grant_type', 'password')

      fetch('http://0.0.0.0:8000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          Accept: 'application/json'
        },
        body: formData.toString()
      })
        .then((response) => {
          if (!response.ok) {
            let errorMessage = 'Unknown error occurred.'

            if (response.status === 400) {
              errorMessage = 'Invalid data. Please check your input and try again.'
            } else if (response.status === 401) {
              errorMessage = 'Incorrect email or password'
            } else if (response.status === 500) {
              errorMessage = 'Server error. Please try again later.'
            }

            alert(errorMessage)
            return Promise.reject(new Error(errorMessage))
          }
          return response.json()
        })
        .then((data) => {
          const { access_token, refresh_token } = data

          if (access_token && refresh_token) {
            localStorage.setItem('accessToken', access_token)

            document.cookie = `refreshToken=${refresh_token}; path=/; max-age=604800; secure; SameSite=Strict`

            router.push({ name: 'UserPage' })
          } else {
            throw new Error('Missing tokens in response')
          }
        })
        .catch((error) => {
          console.error('Error during login:', error.message)
        })
    }

    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      email,
      password,
      goToRegister,
      submitForm
    }
  }
})
