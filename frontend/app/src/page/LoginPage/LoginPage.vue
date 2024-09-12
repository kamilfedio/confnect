<template>
  <div>
    <AuthBackground />
    <div class="loginPage">
      <div class="loginPage__loginForm loginForm">
        <p class="loginForm__text">Again we us. We are so glad you love us!</p>
        <form @submit.prevent="submitForm" class="loginForm__form">
          <input
            type="email"
            class="loginForm__input"
            placeholder="email"
            v-model="email"
            required
          />
          <input
            type="password"
            class="loginForm__input"
            placeholder="password"
            v-model="password"
            required
          />
          <button type="submit" class="loginForm__btn">Get started</button>
        </form>
      </div>
      <div class="loginPage__logo logo">
        <img src="../../img/whiteBlueLogo.png" alt="" />
      </div>
      <div class="loginPage__btn" @click="goToRegister">register</div>
      <div class="loginPage__image">
        <div class="loginPage__part"></div>
      </div>
    </div>
  </div>
</template>

<style src="./LoginPage.scss" scoped></style>
<script src="./LoginPage.vue.ts"></script>
