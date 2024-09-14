import { defineComponent, ref } from 'vue'
import { refreshAccessToken } from '../../utils/auth.js'

export default defineComponent({
  name: 'AddEvent',
  components: {},
  setup() {
    const name = ref<string>('')
    const description = ref<string>('')
    const place = ref<string>('')
    const date = ref<string>('')
    const optional_info = ref<string>('')
    const validationErrors = ref<any>(null) // Zmienna do przechowywania błędów walidacji

    const submitForm = () => {
      validationErrors.value = null // Resetowanie błędów przed wysłaniem nowego żądania

      fetch('http://0.0.0.0:8000/api/v1/events/', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('accessToken')}`, // Pobranie tokena z localStorage
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: name.value,
          description: description.value,
          place: place.value,
          date: date.value,
          optional_info: optional_info.value
        })
      })
        .then((response) => {
          if (!response.ok) {
            if (response.status === 401) {
              return refreshAccessToken().then(() => {
                return fetch('http://0.0.0.0:8000/api/v1/events/', {
                  method: 'POST',
                  headers: {
                    Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                    name: name.value,
                    description: description.value,
                    place: place.value,
                    date: date.value,
                    optional_info: optional_info.value
                  })
                })
              })
            }
            throw new Error(`Request failed with status ${response.status}`)
          }
          return response.json()
        })
        .then((data) => {
          console.log('Success:', data)
        })
        .catch((error) => {
          console.error('Error:', error.message)
        })
    }

    // Zwracamy zmienne i funkcje, które będą używane w szablonie
    return {
      name,
      description,
      place,
      date,
      optional_info,
      validationErrors, // Zwracamy błędy walidacji
      submitForm
    }
  }
})
