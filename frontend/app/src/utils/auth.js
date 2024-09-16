// Pobranie refresh tokena
export const getRefreshTokenFromCookies = () => {
  const value = `; ${document.cookie}`
  const parts = value.split(`; refreshToken=`)
  if (parts.length === 2) return parts.pop()?.split(';').shift() || null
  return null
}

// Sprawdzenie, czy użytkownik jest zalogowany na podstawie obecności access token
export const isAuthenticated = () => {
  const refreshToken = getRefreshTokenFromCookies()
  return !!refreshToken
}

// Aktualizacja access tokena
export const refreshAccessToken = () => {
  const refreshToken = getRefreshTokenFromCookies()

  if (!refreshToken) {
    console.error('Refresh token is missing')
    return Promise.reject(new Error('Refresh token is missing'))
  }

  const refreshUrl = `http://0.0.0.0:8000/refresh?refresh_token=${refreshToken}`

  return fetch(refreshUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
    body: JSON.stringify({})
  })
    .then((response) => {
      return response.json()
    })
    .then((data) => {
      const { access_token } = data
      localStorage.setItem('accessToken', access_token)
    })
    .catch((error) => {
      console.error('Error refreshing access token:', error)
      return Promise.reject(error)
    })
}
