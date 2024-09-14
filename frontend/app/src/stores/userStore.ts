import { defineStore } from 'pinia'
import { refreshAccessToken } from '../utils/auth.js'

interface Event {
  name: string
  description: string
  place: string
  date: string
  optional_info: string
  status: string
}

// Definiowanie store dla użytkownika
export const useUserStore = defineStore('user', {
  state: () => ({
    events: [] as Event[]
  }),

  actions: {
    fetchUserEvents() {
      fetch('http://0.0.0.0:8000/api/v1/events/', {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          if (!response.ok) {
            if (response.status === 401) {
              return refreshAccessToken().then(() => {
                return fetch('http://0.0.0.0:8000/api/v1/events/', {
                  method: 'GET',
                  headers: {
                    Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
                    'Content-Type': 'application/json'
                  }
                })
              })
            }
            throw new Error('Failed to fetch events')
          }
          return response.json()
        })
        .then((data) => {
          this.events = data
          console.log(this.events)
        })
        .catch((error) => {
          console.error('Error fetching events:', error.message)
        })
    }
  }
})
