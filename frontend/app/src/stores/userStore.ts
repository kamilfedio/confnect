import { defineStore } from 'pinia'

// Interfejs dla danych użytkownika
interface User {
  email: string
  name: string
}

// Definiowanie store dla użytkownika
export const useUserStore = defineStore('user', {
  state: () => ({
    accessToken: null as string | null
  }),

  actions: {
    // Zapisanie access tokena w store
    setAccessToken(token: string) {
      this.accessToken = token
    },

    // Usunięcie access tokena (np. podczas wylogowania)
    clearAccessToken() {
      this.accessToken = null
    }
  },

  getters: {
    // Sprawdzenie, czy użytkownik jest zalogowany
    isLoggedIn: (state): boolean => !!state.accessToken
  }
})
