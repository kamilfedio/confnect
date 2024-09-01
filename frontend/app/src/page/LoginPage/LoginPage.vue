<template>
  <div>
    <AuthBackground />
    <div class="loginPage">
      <div class="loginPage__loginForm loginForm"></div>
      <div class="loginPage__logo logo">
        <img src="../../img/whiteBlueLogo.png" alt="" />
      </div>
      <div class="loginPage__btn" @click="goToRegister">login</div>
      <div class="loginPage__image">
        <div class="loginPage__part"></div>
      </div>
    </div>
  </div>
</template>

<style src="./LoginPage.scss" scoped></style>
<script src="./LoginPage.vue.ts"></script>
