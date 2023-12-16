<template>
  <main>
    <form ref="form" @submit.prevent>
      <h2>Login ✨</h2>
      <div class="inputs">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" />
        <label for="password">Password</label>
        <input type="password" id="password" name="password" />
      </div>

      <p class="text">not have account yet? <RouterLink to="">register now!</RouterLink></p>
      <button class="submit" @click="login" type="submit">Login</button>
    </form>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref(null)
const API_URL = 'http://127.0.0.1:8080/api/auth/token'

function login() {
  if (!form.value) return

  const formData = new FormData(form.value)

  const body = Object.fromEntries(
    new URLSearchParams({
      username: formData.get('username'),
      password: formData.get('password')
    })
  )

  // fetch data via post in x-www-urlencoded
  fetch(`${API_URL}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams(body)
  }).then((res) => {
    if (res.ok) {
      res.json().then((data) => {
        localStorage.setItem('token', data.access_token)
        localStorage.setItem('user_id', data.user_id)

        sendTokenToChromeExtension({
          extensionId: 'egeojfmnocaggbciaeejlinjplkpidnc',
          jwt: data.access_token
        })

        router.push({ name: 'home' })
      })
    } else {
      throw new Error('Something went wrong')
    }
  })
}

const sendTokenToChromeExtension = ({ extensionId, jwt }) => {
  chrome.runtime.sendMessage(extensionId, { jwt }, (response: any) => {
    if (!response.success) {
      console.log('error sending message', response)
      return response
    }
    console.log('Sucesss ::: ', response.message)
  })
}
</script>

<style scoped>
main {
  height: 80vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}

.inputs {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.text {
  font-size: 0.8rem;
  letter-spacing: 1px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

input[type='text'],
input[type='password'] {
  padding: 10px;
  font-size: 1.6rem;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.submit {
  background-color: #66afe9;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 1.6rem;
  font-weight: bold;
  border-radius: 5px;
}

.submit:hover {
  background-color: #00254d;
  transition: 0.3s;
  cursor: pointer;
}
</style>
