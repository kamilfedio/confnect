import { useUserStore } from '@/stores/userStore'

// Sprawdzenie, czy użytkownik jest zalogowany na podstawie obecności access tokena w Pinia Store
export const isAuthenticated = () => {
  const userStore = useUserStore()
  return !!userStore.accessToken
}
