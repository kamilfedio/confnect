// Sprawdzenie, czy użytkownik jest zalogowany na podstawie obecności access token
export const isAuthenticated = () => {
  const accessToken = localStorage.getItem('accessToken')
  return !!accessToken // Zwraca true, jeśli token istnieje, false w przeciwnym razie
}

// Funkcja logowania - zapisuje tokeny w localStorage
export const login = ({ accessToken, refreshToken, tokenType }) => {
  localStorage.setItem('accessToken', accessToken)
  localStorage.setItem('refreshToken', refreshToken)
  localStorage.setItem('tokenType', tokenType || 'Bearer') // Domyślnie "Bearer", jeśli tokenType nie został podany
}

// Funkcja wylogowania - usuwa tokeny z localStorage
export const logout = () => {
  localStorage.removeItem('accessToken')
  localStorage.removeItem('refreshToken')
  localStorage.removeItem('tokenType')
}

// Pobierz access token (np. do użytku w nagłówkach autoryzacji)
export const getAccessToken = () => {
  return localStorage.getItem('accessToken')
}

// Pobierz refresh token
export const getRefreshToken = () => {
  return localStorage.getItem('refreshToken')
}

// Pobierz typ tokena (np. "Bearer")
export const getTokenType = () => {
  return localStorage.getItem('tokenType') || 'Bearer'
}
