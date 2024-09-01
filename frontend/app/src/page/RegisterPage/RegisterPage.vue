<template>
  <div>
    <AuthBackground />
    <div class="registerPage">
      <div class="registerPage__loginForm loginForm"></div>
      <div class="registerPage__logo logo">
        <img src="../../img/whiteBlueLogo.png" alt="" />
      </div>
      <div class="registerPage__btn" @click="goToLogin">Register</div>
      <div class="registerPage__image">
        <div class="registerPage__part"></div>
      </div>
    </div>
  </div>
</template>

<script src="./RegisterPage.vue.ts"></script>
<style src="./RegisterPage.scss" scoped></style>
