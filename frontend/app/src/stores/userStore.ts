import { defineStore } from 'pinia'
import { refreshAccessToken } from '../utils/auth.js'

export interface UserEvent {
  name: string
  description: string
  place: string
  date: string
  optional_info: string
}

// Definiowanie store dla użytkownika
export const useUserStore = defineStore('user', {
  state: () => ({
    events: [] as UserEvent[]
  }),

  actions: {
    async fetchUserEvents() {
      try {
        let response = await fetch('http://0.0.0.0:8000/api/v1/events/', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            'Content-Type': 'application/json'
          }
        })

        if (response.status === 401) {
          await refreshAccessToken()
          response = await fetch('http://0.0.0.0:8000/api/v1/events/', {
            method: 'GET',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
              'Content-Type': 'application/json'
            }
          })
        }
        if (!response.ok) {
          throw new Error('Failed to fetch events')
        }

        const data: UserEvent[] = await response.json()
        this.events = data
      } catch (error) {
        console.error('Error fetching events')
      }
    }
  }
})
